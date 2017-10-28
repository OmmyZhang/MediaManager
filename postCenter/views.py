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

def getNullErrorInfo():
    response_data = {}
    response_data['info'] = 'NULL'
    return response_data


def getNullFileTag():
    response_data = {}
    response_data['id'] = 0
    response_data['name'] = 'NULL'
    response_data['color'] = 'NULL'
    return response_data


def getNullUserGroup():
    response_data = {}
    response_data['id'] = 0
    response_data['name'] = 'NULL'
    return response_data


def getNullFile():
    response_data = {}
    response_data['id'] = 'NULL'
    response_data['isDir'] = false
    response_data['path'] = 'NULL'
    response_data['url'] = 'NULL'
    response_data['md5'] = 'NULL'
    response_data['thumbnails'] = 'NULL'
    response_data['size'] = 0
    response_data['modifyDate'] = '2000-1-1 0:0:0'
    response_data['createDate'] = '2000-1-1 0:0:0'
    response_data['tags'] = getNullFileTag()
    return response_data


def getNullUser():
    response_data = {}
    response_data['id'] = 0
    response_data['username'] = 'NULL'
    response_data['password'] = 'NULL'
    response_data['firstName'] = 'NULL'
    response_data['lastName'] = 'NULL'
    response_data['email'] = 'NULL'
    response_data['phone'] = 'NULL'
    response_data['image'] = 'NULL'
    response_data['groups'] = getNullGroup()
    return response_data


def P_CreatUser(request):
    body = request.Post.get('body')
    data = json.load(body)
    Flag = accounts.views.create_user(data['username'], data['password'], data['email'])
    # Flag is the id
    pass


def G_GetUser(request):
    name = request.Get.get('name')
    group = request.Get.get('group')
    # Now we find user in group
    UserList = setting.views.group_mems(group)
    response_data = []
    for i in UserList:
        User = accounts.views.get_user(i)
        UserJson = createNullUser()
        UserJson['id'] = i
        UserJson['username'] = User.username
        UserJson['firstName'] = User.first_name
        UserJson['lastName'] = User.last_name
        UserJson['email'] = User.email
        UserJson['password'] = User.password
        response_data.append(UserJson)
    return HttpResponse(json.dumps(response_data), content_type="application/json")
    pass


# WRAP : -> NOT FINISH

def P_SignupUser(request):
    body = request.Post.get('body')
    data = json.load(body)
    Flag = accounts.views.create_user(data['username'], data['password'], data['email'])
    # Flag is the id
    pass


def G_LogInUser(request):
    username = request.Get.get('username')
    password = request.Get.get('password')
    user = auth.authenticate(username=username, password=password)
    if user and user.is_active:
        auth.login(request, user)
    pass


# WRAP : -> NOT FINISH

def G_LogOutUser(request):
    auth.logout(request)
    pass


# WRAP : -> NOT FINISH

def G_GetUserByName(request, idstr):
    Id = int(idstr)
    user = accounts.views.getUser(Id)
    response_data = creatNullUser()
    User = accounts.views.get_user(user)
    response_data['id'] = Id
    response_data['username'] = User.username
    response_data['firstName'] = User.first_name
    response_data['lastName'] = User.last_name
    response_data['email'] = User.email
    response_data['password'] = User.password
    return HttpResponse(json.dumps(response_data), content_type="application/json")
    pass


# WRAP : -> NOT FINISH

def U_UpdateUser(request, idstr):
    Id = int(idstr)
    body = request.Put.get('body')
    data = json.load(body)
    User = accounts.view.getUser(Id)
    User.username = data['username']
    User.first_name = data['firstName']
    User.last_name = data['lastName']
    User.email = data['email']
    User.set_password(data['password'])
    User.save()
    pass


def D_DeleteUser(request, idstr):
    Id = int(idstr)
    pass


# WRAP : -> NOT FINISH

def P_CreateGroup(request):
    body = request.Post.get('body')
    data = json.load(body)
    Flag = files.views.new_tag(data['name'], isGroup=False)
    # Group ID
    pass


def G_GetAllGroup(request):
    # No input
    response_data = []
    info = files.views.all_Group()
    for i in info:
        Group = files.views.get_tag(i)
        GroupJson = createNullGroup()
        GroupJson['id'] = i
        GroupJson['name'] = Group.name
        response_data.append(GroupJson)
    return HttpResponse(json.dumps(response_data), content_type="application/json")
    pass


# WRAP : -> NOT FINISH

def G_GetGroupById(request, idstr):
    Id = int(instr)
    response_data = {}
    Group = files.views.get_tag(i)
    response_data['id'] = Id
    response_data['name'] = Group.name
    return HttpResponse(json.dumps(response_data), content_type="application/json")
    pass


def U_UpdateGroup(request, idstr):
    Id = int(idstr)
    body = request.Put.get('body')
    data = json.loads(body)
    Group = files.views.get_tag(Id)
    Group.name = data['name']
    Group.save()
    pass


def D_DeleteGroup(request, idstr):
    Id = int(idstr)
    pass


# WRAP : -> NOT FINISH

def P_CreateFile(request):
    body = request.Post.get('body')
    data = json.loads(body)
    ID = files.views.new_file(data['path'], data['name'])
    Flag = files.views.New(data['path'], data['name'])
    if (Flag == False):
        # Create fail
        pass
    pass


def G_GetFileByQuery(request):
    path = request.Get.get('path')
    name = request.Get.get('name')
    tags = request.Get.get('tags')
    # So we use path first

    pass


# WRAP : -> NOT FINISH

def G_GetFileById(request, idstr):
    Id = int(idstr)
    stFile = files.views.getFile(Id)
    pass


def D_DeleteFile(request, idstr):
    Id = int(idstr)
    Flag = file.views.Remove(Id)
    if (Flag == False):
        # Delete Fail
        pass
    # Delete File
    # Wrap : -> NOT FINISH
    pass


def P_UploadFile(request):
    file = request.Post.get('file')
    path = request.Post.get('Path')
    Flag = file.views.Upload_file(file, path)

    now_user_name = request.user.username

    list = file_show(now_user_name)
    error = ''
    if request.method == "POST":
        now_user_name = request.user.username
        File = request.FILES.get("Upload_file", None)
    if not File:
        error = "no upload file"
    else:
        des_path = "data/" + now_user_name + "/" + File.name
        # We need to create a temp path
        destination = open(des_path, 'wb+')
        for chunk in File.chunks():
            destination.write(chunk)
        destination.close()

    list = file_show(now_user_name)
    # NEED TO REWRITE AND DEBUG
    pass


def DownloadFile(request, idstr):
    Id = int(idstr)
    File = files.views.get_file(Id)
    file_name = File.name
    file_path = "data/" + File.path + "/" + file_name
    #Check it out, it is strange and may hold bugs
    response = StreamingHttpResponse(file_iterator(file_path))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename={0}'.format(file_name.encode('utf8'))
    return response


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
        if (len(Path) > 6):
            if (Path[0:6] == '/user/') & (Path[6] >= '0') & (Path[6] <= '9'):
                G_GetUserByName(request, Path[6:])
        # This is not halal, but we can use it first.
        if (Path == '/group'):
            G_GetAllGroup(request)
        if (Path[0:7] == '/group/'):
            G_GetGroupById(request, Path[7:])
        if (Path == '/file'):
            G_GetFileByQuery(request)
        if (Path[0:6] == '/file/'):
            G_GetFileById(request, Path[6:])
        pass
    if request.method == 'PUT':
        if (Path[0:6] == '/user/'):
            U_UpdateUser(request, Path[6:])
        if (Path[0:7] == '/group/'):
            U_UpdateGroup(request, Path[7:])
        pass
    if request.method == 'DELETE':
        if (Path[0:6] == '/user/'):
            D_DeleteUser(request, Path[6:])
        if (Path[0:7] == '/group/'):
            D_DeleteGroup(request, Path[7:])
        if (Path[0:6] == '/file/'):
            D_DeleteFile(request, Path[6:])
        pass
