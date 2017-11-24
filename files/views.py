#-*-coding:UTF-8-*-
from django.http import HttpResponseRedirect,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
import os,time,shutil
import re
import shutil
from os import path
from django.http import StreamingHttpResponse
from .models import FileToTag,StFile,StTag,FileSerializer,TagSerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework import status,permissions,serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAdminUser

class IsAdminOrAvailable(permissions.BasePermission):
    def has_permission(self, request, view):
        return available_to_file(request.user, int(view.kwargs['pk']))

class TagList(mixins.ListModelMixin,
              mixins.CreateModelMixin,
              generics.GenericAPIView):

    queryset = StTag.objects.filter(isGroup = False)
    serializer_class = TagSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        request.data['isGroup'] = False
        return self.create(request, *args, **kwargs)

class TagById(generics.RetrieveUpdateDestroyAPIView):
    queryset = StTag.objects.filter(isGroup = False)
    serializer_class = TagSerializer

class FileList(APIView):
    def get(self, request, format=None):
        body = request.GET

        if 'path' in body:
            return Response([
                format_file(ff.id)
                for ff in StFile.objects.filter(path = request.GET['path'])
                if available_to_file(request.user, ff.id)
                ])

        if 'name' in body:
            rex = body['name']
            return Response([
                format_file(ff.id)
                for ff in StFile.objects.all()
                if (re.match(rex,ff.name) is not None) and available_to_file(request.user, ff.id)
                ])
        
        if 'tags[]' in body:
            tags = body.getlist('tags[]')
            f = []
            for i in tags:
                fi = tag_files(i)
                f = f + fi
            
            return Response([
                format_file(ff)
                for ff in set(f)
                if available_to_file(request.user, ff)
                ])
        
        return Response({'info':'query Nothing'},
                status=status.HTTP_400_BAD_REQUEST)
        

    def post(self, request, format=None):
        body = request.data
        body['ownerID'] = request.user.id
        body['createDate'] = time.strftime("%Y-%m-%dT%H:%m:%S")
        
        id, resp = create_file_and_resp(body,None)
        return resp
    
    def put(self, request, format=None):
       
        err = []
        for body in request.data:
            id = body['id']
            if not available_to_file(request.user, id):
                err.append({
                    'id':id,
                    'error':'no permission'
                    })
                continue

            f = get_file(id)
            if f.isDir and ('path' in body or 'name' in body):
                old_path = '^' + f.path + f.name +'/'
                new_path = body.get('path', f.path) + body.get('name', f.name) + '/'
                for f in StFile.objects.all():
                    print(old_path, '->', new_path, ' ?? ', f.path)
                    if re.match(old_path, f.path) and available_to_file(request.user, f.id):
                        f.path = re.sub(old_path, new_path, f.path)
                        print('get!')
                        print(f.path)
                        f.save()
            
            serializer = FileSerializer(f, data = body, partial=True)
            if serializer.is_valid():
                serializer.save()
            else:
                err.append({
                    'id':id,
                    'error':serializer.errors
                    })
            print('hhhhh',id)
            print(body)
            print(body['tags'])
            if 'tags' in body and 'shareToGroups' in body:
                FileToTag.objects.filter(file_id = id).delete()
                for t in body['tags']:
                    create_FileToTag(id, t['id'])
                for t in body['shareToGroups']:
                    create_FileToTag(id, t['id'])
            
            if 'videoInfo' in body:
                pass
        
        if err:
            return Response({'info':err},
                    status=status.HTTP_400_BAD_REQUEST)
        return  Response()

def create_file_and_resp(data,fname):
    data['modifyDate'] = time.strftime("%Y-%m-%dT%H:%M:%S")
    
    if fname is None:
        data['size'] = 0
    else:
        data['size'] = os.path.getsize(fname)

    serializer = FileSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        id = serializer.data['id'] 
        return id, Response(format_file(id),
                    status=status.HTTP_201_CREATED)
        
    return None, Response(serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)

    

class FileById(APIView):
    permission_classes = (IsAdminOrAvailable,)

    def get(self, request, pk, format=None):
        return Response(format_file(pk))

    def delete(self, request, pk, format=None):
        f = get_file(pk)
        f.delete()
        FileToTag.objects.filter(file_id = pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


class FileData(APIView):
    #permission_classes = (IsAdminOrAvailable,)

    def post(self, request, pk, format=None):
        
        body = request.data

        f = request.FILES['file']
        path = body['path']
        print(request.user.username)
        fname = request.user.username + ':' + f.name + '.part_' + str(time.time())
        with open('data/'+fname, 'wb+') as des:
            for chunk in f.chunks():
                des.write(chunk)
        
        if int(pk) > 0:
            os.rename('data/'+fname, 'data/'+str(pk))
            oldf = get_file(pk)
            oldf.modifyDate = time.strftime("%Y-%m-%dT%H:%M:%S")
            oldf.name = f.name
            oldf.size = os.path.getsize('data/'+str(pk))
            oldf.save()
            return Response(format_file(pk))


        data = {
                'ownerID': request.user.id,
                'name': f.name,
                'createDate': time.strftime("%Y-%m-%dT%H:%M:%S"),
                'path': path,
                'isDir': False
                }

        pk, resp = create_file_and_resp(data, 'data/'+fname)
    
        os.rename('data/'+fname,'data/'+str(pk))

        return resp

    def get(self, request, pk, format=None):
        
        f = get_file(pk)

        resp = StreamingHttpResponse(file_iterator('data/'+ str(pk)))
        resp['Content-Type'] = 'application/octet-stream'
        resp['Content-Disposition'] = 'attachment;filename="%s"' % f.name.encode('utf-8').decode('ISO-8859-1')

        return resp

#-------------------------

def available_to_file(u, fid):
    if fid == 0:
        return True

    f = get_file(fid)
    if f is None:
        return False
    
    if u.is_superuser or u.id == f.ownerID:
        return True
    
    uid = u.id
    
    from group.views import user_groups
    for g in user_groups(uid):
        if check_FileToTag(fid, g):
            return True
    return False

def format_file(id):
    f = get_file(id)
    serializer = FileSerializer(f)
    data = serializer.data
    data['tags'] =  []
    data['shareToGroups'] = []

    for tid in file_tags(id):
        tt = get_tag(tid)
        dic = {
                'id':tid,
                'name': tt.name,
                'color':tt.color
            }
        if tt.isGroup:
            data['shareToGroups'].append(dic)
        else:
            data['tags'].append(dic)

    return data

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

def files_here(ownerID,path):
    fh = []
    for ff in StFile.objects.filter(ownerID = ownerID, path = path):
        fh.append(ff.id)
    return fh

def new_file(ownerID, path,name):
    newF = StFile(ownerID = ownerID, path = path , name = name)
    newF.save()
    return newF.id

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

