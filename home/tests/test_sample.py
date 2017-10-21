from django.test import TestCase
# Create your tests here.


class SampleTestCase(TestCase):
    def setUp(self):
        pass

    def test_sample1(self):
        """Just a sample test"""
        from setting.views import createBelong,checkBelong,groupMems,userGroups
        createBelong(11,-1)
        createBelong(12,-1)
        createBelong(11,-5)
        print(checkBelong(11,-1))  
        print(groupMems(-1))
        print(userGroups(11))


    def test_sample2(self):
        """Just a sample test"""
        a = 1 + 2
        self.assertEqual(3, a)

