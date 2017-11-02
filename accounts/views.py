from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate , login, logout
from django.contrib.auth.models import User
import os,time
import re
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from setting.views import user_groups,group_mems,create_Belong


# Create your views here.

class OneUser(APIView):
    def get(self, request, format=None):
        if 'name' in request.GET:
            name = request.GET['name']
            users = regex_user(name)
        elif 'group' in request.GET:
            group = request.GET['group']
            users = group_mems(int(group))
        else:
            return Response({"info": "no name and no group"},status=status.HTTP_400_BAD_REQUEST)
        return Response([formate_user(i) for i in users])
    
    def post(self, request, format=None):
        body = request.POST
        print(request.POST)
        uid = create_user(
                body['username'],
                body['passwprd'],
                body['email']
                )
        for g in body[groups]:
            create_Belong(uid,g['id'])
        return Response(status=status.HTTP_201_CREATED) 

def formate_user(id):
    u = get_user(id)
    if u is not None:
        return {
                "id": u.id,
                "username": u.username,
                "password": "NotShow",
                "firstName": u.first_name,
                "lastName": u.last_name,
                "email": u.email,
                "phone": "string",
                "image": "string",
                "groups": user_groups(u.id),
                }
    else:
        return None

def create_user(username,passwd,email):
    newM = User.objects.create_user(username,email,passwd)
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

