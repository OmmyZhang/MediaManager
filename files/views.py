#-*-coding:UTF-8-*-
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
import os
import re
from os import path
from django.http import StreamingHttpResponse
#import mimetypes
#import MimeWriter
#import mimetools

# Create your views here.
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
    response['Content-Disposition'] = 'attachment;filename={0}'.format(file_name.encode('utf8')) 
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
