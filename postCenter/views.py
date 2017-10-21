# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
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
	data = json.load(body)
	Flag = accounts.views.createUser(data['username'], data['password'], data['email'])
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
	Flag = accounts.views.createUser(data['username'], data['password'], data['email'])
	#Flag is the id
	pass

def G_LogInUser(request):
	username = request.Get.get('username')
	password = request.Get.get('password')
	pass
	#WRAP : -> NOT FINISH

def G_LogOutUser(request);
	# No Input there
	pass
	#WRAP : -> NOT FINISH

def G_GetUserByName(request);
	id = request.Get.get('id')
	user = accounts.views.getUser(id);
	pass
	#WRAP : -> NOT FINISH

def U_UpdateUser(request):
	id = request.Put.get('id')
	body = request.Put.get('body')
	data = json.load(user)
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
	Flag = files.views.newTag(data['name'], True)
	#Group ID
	pass

def G_GetAllGroup(request):
	#No input
	pass
	#WRAP : -> NOT FINISH

def G_GetGroupById(request):
	id = request.Get.get('id')
	Flag = files.views.groupMems(id)
	#List of user
	pass

def U_UpdateGroup(request):
	id = request.Put.get('id')
	body = request.Put.get('body')
	data = json.loads(body)
	Group = files.views.getTag(id)
	Group.name = data['name']
	Group.save()
	pass

def D_DeleteGroup(request);
	id = request.Delete.get('id')
	pass
	#WRAP : -> NOT FINISH

def P_CreateFile(request):
	body = request.Post.get('body')
	data = json.loads(body)
	Flag = file.views.New(data['path'], data['name'])
	if (!Flag):
		#Create fail
		pass
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
	Flag = file.views.Remove(id)
	if (!Flag):
		#Delete Fail
		pass
	pass

def P_UploadFile(request):
	file = request.Post.get('file')
	path = request.Post.get('Path')
	Flag = file.views.Save_file(file, path)
	if (!Flag):
		#Upload Fail
		pass
	

def post_Center(request):
	if request.method == 'POST':
		P_UploadFile(request)
	if request.method == 'GET':
		pass
	if request.method == 'PUT':
		pass
	if request.method == 'DELETE':
		D_DeleteFile(request)
