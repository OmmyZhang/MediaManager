#encoding:utf-8
from django.test import TestCase
from .views import *
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
        print(getTag(g1).name)
