#-*-coding:UTF-8-*-
from django.http import HttpResponseRedirect,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import os,time
import re
import shutil
from os import path
from django.http import StreamingHttpResponse
# import mimetypes
# import MimeWriter
# import mimetools
#def Save_file(File, save_path):
#    if not os.path.exists(save_path):
#        return False;
#    try:
#        destination = open(save_path,'wb+')
#        for chunk in File.chunks():
#            destination.write(chunk)
#        destination.close()
#    except:
#        return False;
#    return True;

def Download_file(download_path,file_name):
     download_path = download_path + '/' + file_name;
     if not os.path.exis(download_path):
         return False
     response = StreamingHttpResponse(file_iterator(download_path))
     response['Content-Type'] = 'application/octet-stream'
     response['Content-Disposition'] = 'attachment;filename='+file_name
     return response


def createFileToTag(fi,ti): # create a relationship between file and tag
    assert getFile(fi) is not None , "Wrong file id"
    assert getTag(ti) is not None , "Wrong tag id"
    ft = FileToTag(file_id = fi , tag_id = ti)
    ft.save()

def checkFileToTag(fi,ti): # check if file has this tag
    if FileToTag.objects.filter(file_id = fi , tag_id= ti):
        return True
    else:
        return False

def tagFiles(ti): # show all files(' id) under this tag
    f = []
    for ft in FileToTag.objects.filter(tag_id = ti):
        f.append(ft.file_id)
    return f

def fileTags(fi):# show all tags(' id) that this file has
    t = []
    for ft in FileToTag.objects.filter(file_id = fi):
        t.append(ft.tag_id)
    return t

def getTag(id):
    try:
        return StTag.objects.get(id = id)
    except:
        return None

def getFile(id):
    try:
        return StFile.objects.get(id = id)
    except:
        return None

def newFile(path,name):
    newF = StFile(path = path , name = name)
    newF.save()
    return newF.id

def newTag(name,isGroup = False):
    newT = StTag(name = name, isGroup = isGroup)
    newT.save()
    return newT.id

def file_show(user_name):
    now_user_name = user_name
    file_list = get_list(now_user_name)
    return file_list      
    
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

def mv(path, new_path):
    return copy(path,new_path) and remove(path)

def copy(path, new_path):
    if not os.path.exists(path):
        return False;
    os.system("mv %s %s"%(path,new_path))
    return True

def new(path, Name="New_Folder"):
    if not os.path.exists(path):
        return False;
    if not os.path.isdir(path):
        return False;
    try:
        os.mkdir(path + "/" + Name)
        return True
    except:
        return False

#def list(path):
#    if not os.path.exists(path) or not os.path.isdir(path):
#        return False;
#    try:
#        file_list = os.listdir(path)
#        return file_list
#    except:
#        return False

