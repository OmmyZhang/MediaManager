from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, logic, logout
from django.contrib.auth.models import User
import os,time
import re
from rest_framework import status, permissions
from rest_framework.views import APIview
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser
from setting.views import user_groups, group_mems, create_Belong
from files.views import get_tag

class Remainder(APIView):
    def get(self, request, format=None):
        get = request.GET
        user_id = get['userID']
        after_time = get['afterTime']
        notice_list = get_list(user_id, after_time)
        return Response([formate_notice(i) for i in users])
#----------------------------------

