# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

import accounts.views
import setting.views
import files.views
# Those are the views

from django.contrib.auth.models import User, UserGroup, File, FileTag, ErrorInfo
# Those are the models

def P_CreatUser(request):
	body = request.Post.get('body')
	pass

def G_GetUser(request):
	name = request.Get.get('name')
	group = request.Get.get('group')
	pass

def P_SignupUser(request):
	body = request.Post.get('body')
	pass

def G_LogInUser(request):
	username = request.Get.get('username')
	password = request.Get.get('password')
	pass

def G_LogOutUser(request);
	# No Input there
	pass

def G_GetUserByName(request);
	id = request.Get.get('id')
	pass

def U_UpdateUser(request):
	id = request.Put.get('id')
	body = request.Put.get('body')
	pass

def D_DeleteUser(request):
	id = request.Delete.get('id')
	pass

def P_CreateGroup(request):
	body = request.Post.get('body')
	pass

def G_GetAllGroup(request):
	#No input
	pass

def G_GetGroupById(request):
	id = request.Get.get('id')
	pass

def U_UpdateGroup(request):
	id = request.Put.get('id')
	body = request.Put.get('body')
	pass

def D_DeleteGroup(request);
	id = request.Delete.get('id')
	pass

def P_CreateFile(request):
	body = request.Post.get('body')
	pass

def G_GetFileByQuery(request):
	path = request.Get.get('path')
	name = request.Get.get('name')
	tags = request.Get.get('tags')
	pass

def G_GetFileById(request):
	id = request.Get.get('id')
	pass

def D_DeleteFile(request):
	id = request.Delete.get('id')
	pass

def P_UploadFile(request):
	file = request.Post.get('file')
	path = request.Post.get('Path')
	pass

def post_Center(request):
	if request.method == 'POST':
		pass
	if request.method == 'GET':
		pass
	if request.method == 'PUT':
		pass
	if request.method == 'DELETE':
		pass
