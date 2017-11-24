# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from society.views import *
import os
#IMPORT MORE WHEN MORE INFO ONLINE

from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate
from society import views

factory = APIRequestFactory()

FollowPath1 = '/user/1/following/2'
FollowPath2 = '/user/1/following/3'
FollowingPath = '/user/1/following'
FollowerPath = '/user/2/follower'
CommentPath = '/comment'
CommentPath_Get = '/comment?fileID=TESTFILE&type=star'
#For get-method, we need a special check
NullJson = {}

CommentJson_Star = {}
CommentJson_Score = {}
CommentJson_Comment = {}

CommentJson_Star['id'] = 0
CommentJson_Star['fileID'] = 'TESTFILE'
CommentJson_Star['userID'] = 1
CommentJson_Star['date'] = '2017-11-11T02:37:42.490Z'
CommentJson_Star['type'] = 'star'
CommentJson_Star['star'] = True

CommentJson_Score['id'] = 0
CommentJson_Score['fileID'] = 'TESTFILE'
CommentJson_Score['userID'] = 1
CommentJson_Score['date'] = '2017-11-11T02:38:42.490Z'
CommentJson_Score['type'] = 'score'
CommentJson_Score['score'] = 4


CommentJson_Comment['id'] = 0
CommentJson_Comment['fileID'] = 'TESTFILE'
CommentJson_Comment['userID'] = 1
CommentJson_Comment['date'] = '2017-11-11T02:39:42.490Z'
CommentJson_Comment['type'] = 'comment'



class SampleTestCase(TestCase):
    def setUp(self):
        pass
    def test_
'''
    def test_sample2(self):
        request = factory.post(FollowPath2)
        #force_authenticate(request, user=user)  #This is not necessary
        view = followSb.as_view()
        response = view(request)

    def test_sample3(self):
        request = factory.get(FollowingPath)
      #  force_authenticate(request, user=user)  #This is not necessary
        view = getFolloweeList.as_view()
        response = view(request)

    def test_sample4(self):
        request = factory.get(FollowerPath)
#force_authenticate(request, user=user)  #This is not necessary
        view = getFolloweeList.as_view()
        response = view(request)

    def test_sample5(self):
        request = factory.delete(FollowPath2)
       # force_authenticate(request, user=user)  #This is not necessary
        view = followSb.as_view()
        response = view(request)

    def test_sample6(self):
        request = factory.put(CommentPath, CommentJson_Comment, format='json')
    #force_authenticate(request, user=user)  #This is not necessary
        view = followSb.as_view()
        response = view(request)

    def test_sample7(self):
        request = factory.put(CommentPath, CommentJson_Star, format='json')
#force_authenticate(request, user=user)  #This is not necessary
        view = followSb.as_view()
        response = view(request)

    def test_sample8(self):
        request = factory.put(CommentPath, CommentJson_Score, format='json')
#force_authenticate(request, user=user)  #This is not necessary
        view = followSb.as_view()
        response = view(request)

    def test_sample9(self):
        request = factory.get(CommentPath_Get)
#force_authenticate(request, user=user)  #This is not necessary
        view = followSb.as_view()
        response = view(request)


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
    '''
# Create your tests here.

