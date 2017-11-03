from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

import os,time
import re
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser
from setting.views import user_groups, group_mems, create_Belong
from files.views import get_tag
from .models import Notice

class Remainder():
    def get(self, request, format=None):
        get = request.GET
        user_id = get['userID']
        after_time = get['afterTime']
        notice_list = getList(user_id, after_time)
        return Response(notice_list)
#----------------------------------

def getNotice(_user, _content):
    time_token = time.time()
    try:
        Notice.object.create(userId = _user, content = _content, time = time_token)
    except:
        return False
    return True

def getList(_user, after_time):
    notice_list = []
    time_token = timeParser(after_time)
    for item in Notice.object.filter(userId = _user):
        if(time_token < item.time):
            notice_list.append(noticeFormat(item.userId, item.content, item.time))
    return notice_list

def timeParser(time_string):
    format_time = time_string.split(".")[0]
    time_tuple = time.strptime(format_time, "%Y-%m-%dT%X")
    return time.mktime(time_tuple)

def noticeFormat(_userId, _content, _time):
    date = time.strftime("%Y-%m-%dT%X", _time)
    date = date + ".000Z"
    return {
            "date":date,
            "content":content,
            }

    
