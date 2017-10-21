#-*-coding:UTF-8-*-
from django.http import HttpResponseRedirect,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import os
import re
from os import path
from django.http import StreamingHttpResponse

# Create your views here.
@csrf_exempt
def Save_file(File, save_path):
    if not os.path.exists(save_path):
        return False;
    try:
        destination = open(save_path,'wb+')
        for chunk in File.chunks():
            destination.write(chunk)
        destination.close()
    except:
        return False;
    return True;
from .models import FileToGroup

def createRelationship(fu,gn): # create a relationship between file and group 
    fg = FileToGroup(file_url = fu , group_name = gn)
    fg.save()

def checkRelationship(fu,gn): # check if file belong to this group
    if FileToGroup.objects.filter(file_url = fu , group_name = gn):
        return True
    else:
        return False

def groupFiles(gn): # show all files in the group
    f = []
    for fg in FileToGroup.objects.filter(group_name = gn):
        f.append(fg.file_url)
    return f

def fileGroups(fu):# show all groups that the file belong to
    gn = []
    for fg in FileToGroup.objects.filter(file_url = fu):
        gn.append(fg.group_name)
    return gn



@login_required
def index(request):
    return HttpResponse("File")

def get_list(user_name):
    path = "data/" + user_name
    answer = []
    for root,dirs,files in os.walk(path):
        answer = files
    return answer

def file_show(user_name):
    now_user_name = user_name
    file_list = get_list(now_user_name)
    return file_list

@csrf_exemptdef 
def Read_file(download_path):
    if not os.path.exists(download_path):
        return False
    try:
        return file_terator(download_path)
    except:
        return False        
    
def file_iterator(file_name, chunck_size = 512):
    with open(file_name,'rb+') as f:
        while True:
            c = f.read(chunck_size)
            if c:
                yield c
            else:
                break
        f.close()

def Remove(path):
    if not os.path.exists(path):
        return False;
    if os.path.isfile(path):
        os.remove(path)
        return True
    if os.path.isdir(path):
        os.rmdir(path)
        return True

def RM(path, new_path):
    if not os.path.exists(path):
        return False;
    os.system("mv %s %s"%(path,new_path))
    Remove(path)
    return True

def New(path, Name="New_Folder"):
    if not os.path.exists(path):
        return False;
    if not os.path.isdir(path):
        return False;
    try:
        os.mkdir(path + "/" + Name)
        return True
    except:
        return False
