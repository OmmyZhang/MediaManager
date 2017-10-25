#encoding:utf-8
from django.test import TestCase
from .views import *
from accounts.views import *
from setting.views import *
# Create your tests here.

class SampleTestCase(TestCase):
    def setUp(self):
        pass

    def test_sample1(self):
        """Just a sample test"""
        usr = create_user('用户1','passwd','1@1.com')
       
        f1 = new_file(usr,'/photo/','1.png')
        f2 = new_file(usr,'/photo/','2.png')
        print(f1)
        print(f2)
        t1 = new_tag('pic')
        g1 = new_tag('贵系',True)
        g2 = new_tag('软件',True)
        create_FileToTag(f1,t1)
        create_FileToTag(f1,g1)
        create_FileToTag(f2,t1)
        print(check_FileToTag(f1,t1))
        print(tag_files(g1))
        print(file_tags(f1))
        print('file1: ',get_file(f1))
        print('tag1: ',get_tag(t1))
        print('group1: ',get_tag(g1))

        print(usr)
        create_Belong(usr,g1)
        
        uu = get_user(usr)

        uu.username = 'user1'
        uu.save()

        usr2 = create_user('用户2','passwd','1@2.com')

        create_Belong(usr2,g1)
        print(group_mems(g1))

        for ur in group_mems(g1):
            print(get_user(ur).username)
            print(get_user(ur).email)

        print(all_group())
        for gg in all_group():
            print('group:',get_tag(gg))

        print(files_here(usr,'/photo/'))
