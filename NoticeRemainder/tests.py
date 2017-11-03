from django.test import TestCase
from .views import sentNotice, getList
import time
class SampleTestCase(TestCase):
    def setUp(self):
        pass
    def test_notice(self):
        str1 = "春风桃李花开日"
        str2 = "秋雨梧桐叶落时"
        str3 = "西宫南内多秋草"
        str4 = "落叶满阶红不扫"
        
        time0 = time.time()
        T0 = time.localtime(time0)
        time.sleep(5)

        self.assertEqual(sentNotice(1, str1), True)
        time1 = time.time()
        T1 = time.localtime(time1)
        print("insert %s at %s\n" %(str1,time.ctime(time1)))
        
        time.sleep(5)
        
        self.assertEqual(sentNotice(2, str2), True)
        time2 = time.time()
        T2 = time.localtime(time2)
        print("insert %s at %s\n" %(str2,ctime(time2)))
        
        time.sleep(5)
        
        self.assertEqual(sentNotice(1, str3), True)
        time3 = time.time()
        T3 = time.localtime(time3)
        print("insert %s at %s\n"%(str3,ctime(time3)))

        time.sleep(5)

        self.assertEqual(sentNotice(2,str4),True)
        time4 = time.time()
        T4 = time.localtime(time4)
        print("insert %s at %s\n" %(str4,ctime(time4)))
        
        form = "%Y-%m-%dT%X.000Z"
        
        after_time0 = time.strftime(form, T0)
        print("after_time0 is %s\n"%after_time0)
        
        after_time1 = time.strftime(form, T1)
        print("after_time1 is %s\n"%after_time1)
        
        after_time2 = time.strftime(form, T2)
        print("after_time2 is %s\n"%after_time2)

        after_time3 = time.strftime(form, T3)
        print("after_time3 is %s\n"%after_time3)

        after_time4 = time.strftime(form, T4)
        print("after_time4 is %s\n"%after_time4)

        print("User1: \n")
        print(getList(1,after_time0))
        print(getList(1,after_time1))
        print(getList(1,after_time2))
        print(getList(1,after_time3))
        print(getList(1,after_time4))

        print("User2: \n")
        print(getList(2,after_time0))
        print(getList(2,after_time1))
        print(getList(2,after_time2))
        print(getList(2,after_time3))
        print(getList(2,after_time4))

