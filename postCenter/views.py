# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.

def P_CreatUser(request):
	pass

def G_GetUser(request):
	pass

def P_SignupUser(request):
	pass

def G_LogInUser(request):
	pass

def G_LogOutUser(request);
	pass

def G_GetUserByName(request);
	pass

def U_UpdateUser(request):
	pass

def D_DeleteUser(request):
	pass

def P_CreateGroup(request):
	pass

def G_GetAllGroup(request):
	pass

def G_GetGroupById(request):
	pass

def U_UpdateGroup(request):
	pass

def D_DeleteGroup(request);
	pass

def P_CreateFile(request):
	pass

def G_GetFileByQuery(request):
	pass

def G_GetFileById(request):
	pass

def D_DeleteFile(request):
	pass

def P_UploadFile(request):
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
