from django.test import TestCase
# Create your tests here.

class SampleTestCase(TestCase):
    def setUp(self):
        pass

    def test_sample1(self):
        """Just a sample test"""
        from .views import createRelationship,checkRelationship,groupFiles,fileGroups
        createRelationship('photo/1.png','group1')
        createRelationship('code/sp.py','group1')
        createRelationship('photo/1.png','group2')
        print(checkRelationship('photo/1.png','group1'))
        print(groupFiles('group1'))
        print(fileGroups('photo/1.png'))
