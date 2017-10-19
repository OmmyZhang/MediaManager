#-*-coding:UTF-8-*-
from django.http import HttpResponseRedirect,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import os
import re
from os import path
from django.http import StreamingHttpResponse

# Create your views here.
@csrf_exempt
def Upload_file(File, save_path):
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

@csrf_exempt
def Download_file(download_path):
    if not os.path.exists(download_path):
        return False
    try:
        response = StreamingHttpResponse(file_iterator(download_path))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename={0}'.format(file_name) 
    except:
        return False
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

