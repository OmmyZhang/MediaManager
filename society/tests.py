# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from society.views import *
import os
#IMPORT MORE WHEN MORE INFO ONLINE

class SampleTestCase(TestCase):
    def setUp(self):
        pass

    def test_sample1(self):
        print(followSb(1, 2))
        print(followSb(1, 2))
        print(followSb(2, 3))
        print(len(getFollowerList(2)))
        print(len(getFolloweeList(3)))
        print(StarFile(1, 2))
        print(len(getStarList(1)))
        print(len(getAllStarer(2)))
        print(StarFile(1, 2))
        postComment(1, 2, 'This is test');
        Temp = getComment(2);
        Temp2 = Temp[0]
        print (Temp2[1])
        removeFile(2)
# Create your tests here.

