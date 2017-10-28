#-*-coding:UTF-8-*-
from django.http import HttpResponseRedirect,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import os,time,shutil
import re
import shutil
from os import path
from django.http import StreamingHttpResponse
from .models import FileToTag,StFile,StTag

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

def file_show(user_name):
    now_user_name = user_name
    file_list = get_list(now_user_name)
    return file_list      
        
#------------------------------------------------------------------------
def Download_file(download_path,file_name):
     download_path = download_path + '/' + file_name;
     if not os.path.exis(download_path):
         return False
     response = StreamingHttpResponse(file_iterator(download_path))
     response['Content-Type'] = 'application/octet-stream'
     response['Content-Disposition'] = 'attachment;filename='+file_name
     return response
         
def file_iterator(file_name, chunck_size = 512):
    with open(file_name,'rb+') as f:
        while True:
            c = f.read(chunck_size)
            if c:
                yield c
            else:
                break
        f.close()

def remove(path):
    if not os.path.exists(path):
        return False;
    if os.path.isfile(path):
        os.remove(path)
        return True
    if os.path.isdir(path):
        shutil.rmtree(path)
        return True

def rename(path, new_name):
    if not os.path.exists(path):
        return False
    try:
        dirname = os.path.dirname(path)
        new_path = os.path.join(dirname,new_name)
        os.system("mv %s %s"%(path,new_path))
    except:
        return False
    return True

def move(src, dst_path):
    if not os.path.exists(src):
        return False
    try:
        filename = os.path.basename(src)
        dst = os.path.join(dst_path,filename)
        os.system("mv %s %s"%(src,dst))
    except:
        return False
    return True

def copy(src, dst_path):
    if not os.path.exists(src):
        return False;
    try:
        filename = os.path.basename(src)
        dst = os.path.join(dst_path,filename)
        shutil.copy(src,dst)
    except:
        return False
    return True

def new(path, name="New_Folder"):
    if not os.path.exists(path):
        return False;
    if not os.path.isdir(path):
        return False;
    try:
        os.mkdir(path + "/" + name)
        return True
    except:
        return False

