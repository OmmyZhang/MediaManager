from django.test import TestCase

# Create your tests here.


class SampleTestCase(TestCase):
    def setUp(self):
        pass

    def test_sample1(self):
        """Just a sample test"""
        a = 1 + 2
        self.assertEqual(3, a)

    def test_sample2(self):
        """Just a sample test"""
        a = 1 + 2
        self.assertEqual(3, a)
