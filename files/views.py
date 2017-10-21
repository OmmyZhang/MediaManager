#-*-coding:UTF-8-*-
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render_to_response
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

        
#------------------------------------------------------------------------

@login_required
def index(request):
    return HttpResponse("File")

def get_list(user_name):
    path = "data/" + user_name
    answer = []
    for root,dirs,files in os.walk(path):
        answer = files
    return answer

@login_required
@csrf_exempt
def Upload_file(request):
    now_user_name = request.user.username
    list = file_show(now_user_name)
    error = ''
    if request.method == "POST":
        now_user_name = request.user.username
        File = request.FILES.get("Upload_file",None)

        #file_bag = get_list(now_user_name)
        #file_list = file_bag(2)
        #for item in file_list:
        #    i

        if not File:
            error = "no upload file"
        else:
            des_path = "data/" + now_user_name + "/" + File.name
            destination = open(des_path,'wb+')
            for chunk in File.chunks():
                destination.write(chunk)
            destination.close()
            error = "upload over"

        list = file_show(now_user_name)

    return render(request,'files/file.html',{'n':now_user_name,'e':error,'File_list':list})

def file_show(user_name):
    now_user_name = user_name
    file_list = get_list(now_user_name)
    return file_list

@login_required
@csrf_exempt
def Download_file(request):
    now_user_name = request.user.username
    file_name = request.POST['File_name']
    file_path = "data/" + now_user_name + "/" + file_name
    #print(file_path)
    response = StreamingHttpResponse(file_iterator(file_path))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename={0}'.format(file_name.encode('utf-8'))
    return response

@csrf_exempt
def file_iterator(file_name, chunck_size = 512):
    with open(file_name,'rb+') as f:
        while True:
            c = f.read(chunck_size)
            if c:
                yield c
            else:
                break
        f.close()
