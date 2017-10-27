from django.test import TestCase
from files.views import *
from setting.views import *
from accounts.views import *
import os
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

        for ur in group_mems(g1):
            print(get_user(ur).username)
            print(get_user(ur).email)
        
        print(files_here(usr,'/photo/'))
    
    def test_sample2(self): #Test for making new dir and delete a simple dir, copy a simple file
        temp_path = "data"
        temp_file = "data/test/loss.py"

        new(temp_path,'weijy')
        new_path = os.path.join(temp_path,'weijy')
        print("create new path:  %s"%new_path)
        self.assertEqual(os.path.exists(new_path), True)
        
        remove(new_path)
        print("remove path: %s"%new_path)
        self.assertEqual(os.path.exists(new_path), False)
    
        self.assertEqual(os.path.exists(temp_file),True)
        remove(temp_file)
        print("remove file: %s"%temp_file)
        self.assertEqual(os.path.exists(temp_file),False)

    def test_sample3(self): #Test  removing a comlex dir
        temp_path = "data/complex"


        self.assertEqual(os.path.exists(temp_path), True)
        remove(temp_path)
        print("remove complex path: %s"%temp_path)
        self.assertEqual(os.path.exists(temp_path),False)
