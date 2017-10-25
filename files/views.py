#-*-coding:UTF-8-*-
from django.http import HttpResponseRedirect,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import os,time
import re
from os import path
from django.http import StreamingHttpResponse
from .models import FileToTag,StFile,StTag
# import mimetypes
# import MimeWriter
# import mimetools

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

def create_FileToTag(fi,ti): # create a relationship between file and tag
    assert get_file(fi) is not None , "Wrong file id"
    assert get_tag(ti) is not None , "Wrong tag id"
    ft = FileToTag(file_id = fi , tag_id = ti)
    ft.save()

def check_FileToTag(fi,ti): # check if file has this tag
    if FileToTag.objects.filter(file_id = fi , tag_id= ti):
        return True
    else:
        return False

def tag_files(ti): # show all files(' id) under this tag
    f = []
    for ft in FileToTag.objects.filter(tag_id = ti):
        f.append(ft.file_id)
    return f

def file_tags(fi):# show all tags(' id) that this file has
    t = []
    for ft in FileToTag.objects.filter(file_id = fi):
        t.append(ft.tag_id)
    return t

def get_tag(id):
    try:
        return StTag.objects.get(id = id)
    except:
        return None
def all_group():
    gs = []
    for tt in StTag.objects.filter(isGroup = True):
        gs.append(tt.id)
    return gs

def get_file(id):
    try:
        return StFile.objects.get(id = id)
    except:
        return None

def files_here(owner,path):
    fh = []
    for ff in StFile.objects.filter(owner = owner, path = path):
        fh.append(ff.id)
    return fh

def new_file(owner, path,name):
    newF = StFile(owner = owner, path = path , name = name)
    newF.save()
    return newF.id

def new_tag(name,isGroup = False):
    newT = StTag(name = name, isGroup = isGroup)
    newT.save()
    return newT.id

        
#------------------------------------------------------------------------


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

@csrf_exempt 
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
