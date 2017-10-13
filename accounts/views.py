from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate , login, logout
from django.contrib.auth.models import User
import os

# Create your views here.

def login_view(request):
    try:
        go_url = request.GET['next']
    except:
        go_url = '/'

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

