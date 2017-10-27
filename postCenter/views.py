# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib import auth

import accounts.views
import setting.views
import files.views
import re
# Those are the views

from django.contrib.auth.models import User, UserGroup, File, FileTag, ErrorInfo
# Those are the models

def P_CreatUser(request):
	body = request.Post.get('body')
	data = json.load(body)
	Flag = accounts.views.create_user(data['username'], data['password'], data['email'])
	#Flag is the id
	pass

def G_GetUser(request):
	name = request.Get.get('name')
	group = request.Get.get('group')
	pass
	#WRAP : -> NOT FINISH

def P_SignupUser(request):
	body = request.Post.get('body')
	data = json.load(body)
	Flag = accounts.views.create_user(data['username'], data['password'], data['email'])
	#Flag is the id
	pass

def G_LogInUser(request):
	username = request.Get.get('username')
	password = request.Get.get('password')
	user = auth.authenticate(username=username, password=password)
	if user and user.is_active:
		auth.login(request, user)
	pass
	#WRAP : -> NOT FINISH

def G_LogOutUser(request):
	auth.logout(request)
	pass
	#WRAP : -> NOT FINISH

def G_GetUserByName(request):
	id = request.Get.get('id')
	user = accounts.views.getUser(id);
	pass
	#WRAP : -> NOT FINISH

def U_UpdateUser(request):
	id = request.Put.get('id')
	body = request.Put.get('body')
	data = json.load(body)
	User = accounts.view.getUser(id)
	User.username = data['username']
	User.first_name = data['firstName']
	User.last_name = data['lastName']
	User.email = data['email']
	User.set_password(data['password'])
	User.save()
	pass

def D_DeleteUser(request):
	id = request.Delete.get('id')
	pass
	#WRAP : -> NOT FINISH

def P_CreateGroup(request):
	body = request.Post.get('body')
	data = json.load(body)
	Flag = files.views.new_tag(data['name'], isGroup = False)
	#Group ID
	pass

def G_GetAllGroup(request):
	#No input
	info = files.views.all_Group()
	pass
	#WRAP : -> NOT FINISH

def G_GetGroupById(request):
	id = request.Get.get('id')
	Flag = setting.views.group_mems(id)
	#List of user
	pass

def U_UpdateGroup(request):
	id = request.Put.get('id')
	body = request.Put.get('body')
	data = json.loads(body)
	Group = files.views.get_tag(id)
	Group.name = data['name']
	Group.save()
	pass

def D_DeleteGroup(request):
	id = request.Delete.get('id')
	pass
	#WRAP : -> NOT FINISH

def P_CreateFile(request):
	body = request.Post.get('body')
	data = json.loads(body)
	ID = files.views.new_file(data['path'], data['name'])
	Flag = files.views.New(data['path'], data['name'])
	if (Flag == False):
		#Create fail
		pass
	pass

def G_GetFileByQuery(request):
	path = request.Get.get('path')
	name = request.Get.get('name')
	tags = request.Get.get('tags')
	pass
	#WRAP : -> NOT FINISH

def G_GetFileById(request):
	id = request.Get.get('id')
	stFile = files.views.getFile(id)
	pass

def D_DeleteFile(request):
	id = request.Delete.get('id')
	Flag = file.views.Remove(id)
	if (Flag == False):
		#Delete Fail
		pass
	#Delete File
	#Wrap : -> NOT FINISH
	pass

def P_UploadFile(request):
	file = request.Post.get('file')
	path = request.Post.get('Path')
	Flag = file.views.Upload_file(file, path)
	if (Flag == False):
		#Upload Fail
		pass

def post_Center(request):
	Path = request.path
	if request.method == 'POST':
		if (Path == '/user'):
			P_CreatUser(request)
		if (Path == '/user/signup'):
			P_SignupUser(request)
		if (Path == '/group'):
			P_CreateGroup(request)
		if (Path == '/file'):
			P_CreateFile(request)
		if (Path == '/file/upload'):
			P_UploadFile(request)
		pass
	if request.method == 'GET':
		if (Path == '/user'):
			G_GetUser(request)
		if (Path == '/user/login'):
			G_LogInUser(request)
		if (Path == '/user/logout'):
			G_LogOutUser(request)
		# "/user/id" is not finished, wait for it....
		if (Path == '/group'):
			G_GetAllGroup(request)
		if (Path[0:7] == '/group/'):
			G_GetGroupById(request)
		if (Path == '/file'):
			G_GetFileByQuery(request)
		if (Path[0:6] == '/file/'):
			G_GetFileById(request)
		#Finish ID Check in debug mode
		pass
	if request.method == 'PUT':
		if (Path[0:6] == '/user/'):
			U_UpdateUser(request)
		if (Path[0:7] == '/group/'):
			U_UpdateGroup(request)
		#Finish ID Check in debug mode
		pass
	if request.method == 'DELETE':
		if (Path[0:6] == '/user/'):
			D_DeleteUser(request)
		if (Path[0:7] == '/group/'):
			D_DeleteGroup(request)
		if (Path[0:6] == '/file/'):
			D_DeleteFile(request)
		#Finish ID Check in debug mode
		pass
