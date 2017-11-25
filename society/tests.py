# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from society.views import *
import os
#IMPORT MORE WHEN MORE INFO ONLINE
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate

from django.contrib.auth.models import User

from society import views
from django.urls import reverse
import json

factory = APIRequestFactory(enforce_csrf_checks=True)

FollowPath1 = '/user/1/following/2'
FollowPath2 = '/user/1/following/3'
FollowingPath = '/user/1/following'
FollowerPath = '/user/2/follower'
CommentPath = '/comment/'
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



class HAHATests(APITestCase):
    def setUp(self):
        kwargs = dict(mobile_phone='12345',password='111111')
        self.user = User.objects.create_user('john','lennon@thebeatles.com','123456789')

    def test_haha(self):
        factory = APIRequestFactory()
        url = reverse('haha')
        data = CommentJson_Comment
        client = APIClient()
        client.login(username='haha2',password='qwert12345')
        #request = factory.post(url,data)
        #force_authenticate(request,user=self.user)
        #resposne = comment.as_view()(request)
        #response = self.client.post(url,data)
        response = client.post(url,data)
        print(response)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
