from django.test import TestCase
from files.views import *
from group.views import *
from accounts.views import *
from files.views import remove,rename,move,copy,new
import os
class SampleTestCase(TestCase):
    def setUp(self):
        pass
    
    def test_sample1(self):
        """Just a sample test"""
        usr = create_user({
            "username":'用户1',
            "password":'passwd',
            "email":'1@1.com'
            })
       
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

        usr2 = create_user({
            "username":'用户2',
            "password":'passwd',
            "email":'1@2.com'
            })

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
    
    '''
    def test_mkdir(self):
        src = "data/debug"
        name = "test"
        new_path = "data/debug/test"
        self.assertEqual(os.path.exists(new_path),False)
        self.assertEqual(new(src,name), True)
        self.assertEqual(os.path.exists(new_path),True)

    def test_copy(self):
        src = "data/Debug.py"
        dst_path = "data/debug"
        dst = "data/debug/Debug.py"
        self.assertEqual(os.path.exists(dst),False)
        self.assertEqual(copy(src,dst_path),True)
        self.assertEqual(os.path.exists(dst),True)

    def test_rename(self):
        src = "data/debug/1.docx"
        new_name = "2.docx"
        new_path = "data/debug/2.docx"
        if not os.path.exists(src):
            src = "data/debug/2.docx"
            new_name = "1.docx"
            new_path = "data/debug/1.docx"
        print("src is ---------------------------->%s"%src)

        self.assertEqual(os.path.exists(new_path),False)
        self.assertEqual(rename(src,new_name),True)
        self.assertEqual(os.path.exists(new_path),True)
    
    def test_move(self):
        src= "data/debug/Debug.py"
        dst_path = "data/debug/test"
                
        new_path = os.path.join(dst_path, os.path.basename(src))
        self.assertEqual(os.path.exists(new_path), False)
        self.assertEqual(os.path.exists(src),True)
        self.assertEqual(move(src, dst_path), True)
        self.assertEqual(os.path.exists(new_path),True)
        self.assertEqual(os.path.exists(src),False)
    
    def test_remove(self):
        src = "data/debug/test"
        self.assertEqual(os.path.exists(src),True)
        self.assertEqual(remove(src),True)
        self.assertEqual(os.path.exists(src),False)
    '''
