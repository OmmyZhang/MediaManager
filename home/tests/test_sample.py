from django.test import TestCase
# Create your tests here.


class SampleTestCase(TestCase):
    def setUp(self):
        pass

    def test_sample1(self):
        """Just a sample test"""
        from setting.views import createBelong,checkBelong,groupMems,userGroups
        createBelong(110,'group1')
        createBelong(120,'group1')
        createBelong(110,'police')
        print(checkBelong(110,'group1'))  
        print(groupMems('group1'))
        print(userGroups(110))


    def test_sample2(self):
        """Just a sample test"""
        a = 1 + 2
        self.assertEqual(3, a)

