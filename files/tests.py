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
       
        f1 = newFile('/photo/','1.png')
        f2 = newFile('/photo/','2.png')
        print(f1)
        print(f2)
        t1 = newTag('pic')
        g1 = newTag('贵系',True)
        createFileToTag(f1,t1)
        createFileToTag(f1,g1)
        createFileToTag(f2,t1)
        print(checkFileToTag(f1,t1))
        print(tagFiles(g1))
        print(fileTags(f1))
        print('file1: ',getFile(f1))
        print('tag1: ',getTag(t1))
        print('group1: ',getTag(g1))

        usr = createUser('用户1','passwd','1@1.com')
        print(usr)
        createBelong(usr,g1)
        
        uu = getUser(usr)

        uu.username = 'user1'
        uu.save()

        usr2 = createUser('用户2','passwd','1@2.com')

        createBelong(usr2,g1)
        print(groupMems(g1))

        for ur in groupMems(g1):
            print(getUser(ur).username)
            print(getUser(ur).email)í
