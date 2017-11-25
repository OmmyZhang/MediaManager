from django.db import IntegrityError
from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate , login, logout
from django.contrib.auth.models import User
import os,time
import re
from rest_framework import status,permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAdminUser
from rest_framework.authtoken.models import Token
from group.views import user_groups,group_mems,create_Belong
from group.models import Belong
from files.views import get_tag


# Create your views here.

class IsAdminOrSelf(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser or (request.user.id == int(view.kwargs['id']))

class OneUser(APIView):
    permission_classes = (IsAdminUser,)
    
    def get(self, request, format=None):
        get = request.GET
        if 'name' in get:
            name = get['name']
            users = regex_user(name)
        elif 'group' in get:
            group = get['group']
            users = group_mems(int(group))
        else:
            return Response({'info': 'no name and no group'},
                    status=status.HTTP_400_BAD_REQUEST)
        return Response([format_user(i) for i in users])
    
    def post(self, request, format=None):
        body = request.data
        try:
            uid = create_user(body)
            for g in body['groups']:
                create_Belong(uid,g['id'])
            return Response(status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'info':repr(e)},
                    status=status.HTTP_400_BAD_REQUEST)

class Signup(APIView):
    permission_classes = (AllowAny,)
    
    def post(self, request, format=None):
        body = request.data
        try:
            uid = create_user(body)
            user = get_user(uid)
            login(request, user)
            token = Token.objects.create(user = user)
            return Response(token.key, status=status.HTTP_201_CREATED)
        except IntegrityError as e:
            return Response({'info': '用户名已存在'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(repr(e))
            #raise e

class Login(APIView):
    permission_classes = (AllowAny,)
    
    def post(self, request, format=None):
        body = request.data
        name   = body['username']
        passwd = body['password']
        user = authenticate(username=name,password=passwd)
        if user is not None:
            login(request,user)
            token  = Token.objects.get_or_create(user = user)[0]
            return Response({'token': token.key, 'userID': user.id})
        else:
            if User.objects.filter(username = name).exists():
                err = 'wrong password'
            else:
                err = 'no users'
            return Response({'info':err},
                    status=status.HTTP_400_BAD_REQUEST)

class Logout(APIView):
    def get(self, request, format=None):
        logout(request)
        return Response()

class UserById(APIView):
    permission_classes = (IsAdminOrSelf,)

    def get(self, request, id, format=None):
        u = format_user(id)
        if u is not None:
            return Response(u)
        else:
            return Response({'info':'No this user'},
                    status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id, format=None):
        u = get_user(id)
        if u is not None:
            body = request.data

            u.username = body['username']
            u.first_name = body['firstName']
            u.email = body['email']
            # TODO 更新 phone

            u.save()
            
            if request.user.is_superuser:
                if body['password']:
                    u.set_password(body['password'])
                Belong.objects.filter(user_id = id).delete()
                for gg in body['groups']:
                    create_Belong(id, gg['id'])

            return Response(format_user(id), status=status.HTTP_200_OK)
        else:
            return Response({'info':'No this user'},
                    status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        u = get_user(id)
        if u is not None:
            u.delete()
            Belong.objects.filter(user_id = id).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'info':'No this user'},
                    status=status.HTTP_400_BAD_REQUEST)

class Passwd(APIView):
    permission_classes = (IsAdminOrSelf,)

    def post(self, request, id, format=None):
        body = request.data
        oldP = body['oldPassword']
        newP = body['newPassword']

        un = get_user(id).username
        testU  = authenticate(username=un,password=oldP)
        if testU is None:
            return Response({'info':'wrong old password'},
                    status=status.HTTP_400_BAD_REQUEST);
        else:
            testU.set_password(newP);
            testU.save();
            return Response()


#-------------------------------------
def format_user(id):
    u = get_user(id)
    if u is not None:
        return {
                'id': u.id,
                'username': u.username,
                'password': 'NotShow',
                'firstName': u.first_name,
                'lastName': u.last_name,
                'email': u.email,
                'phone': 'string',
                'image': 'string',
                'groups': [ {'id':gid,'name':get_tag(gid).name} 
                    for gid in user_groups(u.id) if get_tag(gid) # 可能用户组已经被删除
                    ],
                }
    else:
        return None

def create_user(info):
    newM = User.objects.create_user(
                username = info['username'],
                email = info['email'],
                password = info['password']
                )
    newM.save()
    
    #os.makedirs('data/'+nam)
    
    return newM.id

def get_user(id):
    try:
        return User.objects.get(id = id)
    except:
        return None

def regex_user(rex):
    return [ u.id for u in User.objects.all() 
            if re.match(rex,u.username) is not None ]

#------------------------------------
'''
def login_view(request):
    try:
        go_url = request.GET['next']
    except:
        go_url = '/files/'

    name   = ''
    passwd = ''
    error  = ''
    
    if request.POST:
        name = request.POST['name']
        passwd = request.POST['passwd']
        
        if(not name or not passwd):
            error = 'missInfo'
        
        if(not error):
            try:
                p = User.objects.get(username=name)
            except:
                error = 'notFind'
        
        if(not error):
            user = authenticate(username=name,password=passwd)
            if user is not None:
                login(request,user)
            else:
                error = 'wrongPasswd'

    if request.user.is_authenticated:
        return HttpResponseRedirect(go_url)

    return render(request,'accounts/login.html',{'n':name,'p':passwd,'e':error,'go':go_url})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def register_view(request):
    nam='';mail='';pho='';passwd='';
    err = ''

    if request.POST:
        nam = request.POST['name']
        mail = request.POST['email']
        pho = request.POST['phone']
        passwd = request.POST['password']
        if not ( nam and mail and pho and passwd):
            err = 'missInfo'

        if not err:
                if User.objects.filter(username=nam) or User.objects.filter(email=mail):
                    err = 'alr'
        if not err:
            newM = User.objects.create_user(nam,mail,passwd)
            while(True):
                user_id = str(int(time.time()*1000) % 10000) + str(hash(nam) % 10000)
                if not User.objects.filter(first_name = user_id):
                    break;
            newM.first_name = user_id;
            newM.save()
            login(request,newM)
            try:
                os.makedirs('data/'+nam)
                return HttpResponseRedirect('/')
            except:
                return HttpResponse('<h1>Create dir fail')


    context =   {
                'nam':nam,
                'ema':mail,
                'passwd':passwd,
                'pho':pho,
                'e':err,
                }

    return render(request,'accounts/register.html',context) 
'''
