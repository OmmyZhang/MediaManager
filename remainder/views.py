from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

import os,time
import re
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.views import APIView
from .models import Notice

class Remainder(APIView):
    def get(self, request, format=None):
        get = request.GET
        user_id = request.user.id
        after_time = get['afterTime']
        notice_list = getList(user_id, after_time)
        return Response(notice_list)
#----------------------------------

def sentNotice(_user, _content):
    _time_token = time.time()
   # try:
    Notice.objects.create(userId = _user, content = _content, time_token = _time_token)
   # except:
   #     return False
    return True

def getList(_user, after_time):
    notice_list = []
    time_token = timeParser(after_time)
    for item in Notice.objects.filter(userId = _user):
        if(time_token < item.time_token):
            notice_list.append(noticeFormat(item.userId, item.content, item.time_token))
    return notice_list

def timeParser(time_string):
    format_time = time_string.split(".")[0]
    time_tuple = time.strptime(format_time, "%Y-%m-%dT%X")
    return time.mktime(time_tuple)

def noticeFormat(_userId, _content, _time):
    _Time = time.localtime(_time)
    date = time.strftime("%Y-%m-%dT%X", _Time)
    date = date + ".000Z"
    return {
            "date":date,
            "content":_content,
            }


