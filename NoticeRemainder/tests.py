from django.test import TestCase
from views import sentNotice, getList
import time
class SampleTestCase(TestCase):
    def setUp(self):
        pass
    def test_notice(self):
        str1 = "春风桃李花开日"
        str2 = "秋雨梧桐叶落时"
        str3 = "西宫南内多秋草"
        str4 = "落叶满阶红不扫"

        self.assertEqual(sentNotice(1, str1), True)
        time1 = time.time()
        print("insert %s at %s" %(str1,time.ctime(time1)))
        
        time.sleep(5)
        
        self.assertEqual(sentNotice(2, str2), True)
        time2 = time.time()
        print("insert %s at %s" %(str2,time2))
        
        time.sleep(5)
        
        self.assertEqual(sentNotice(1, str3), True)
        time3 = time.time()
        print("insert %s at %s"%(str3,time3))

        time.sleep(5)
        time4 = time.time()
        print("insert %s
                
