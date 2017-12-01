# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import PeopleFollowPeople, PeopleStarFile, PeopleComment
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
import random
import remainder.views
#More import if needed


class followSb(APIView):   #idone follow idtwo or just cancel
    #followee follow the follower, this is not halal
    def post(self, request, id1, id2, format = None):
        print("---------------------------------------------$$$TEST")
        PeopleFollowPeople.objects.create(followee = id1, follower = id2)
        remainder.views.sentNotice(id2,  str(id1) + ' has followed you! ');
        return Response(status=status.HTTP_200_OK)
    def delete(self, request, id1, id2, format = None):
        PeopleFollowPeople.objects.filter(followee = id1, follower = id2).delete()
        return Response(status=status.HTTP_200_OK)
        # JUMPING : WE CAN SEND A MESSAGE HERE

class getFollowerList(APIView):
    def get(self, request, id1, format = None):
        print("haha")
        pid = id1
        f = []
        for pid in PeopleFollowPeople.objects.filter(followee = id1):
            f.append(pid.follower)
        return Response(f)

class getFolloweeList(APIView): # get all the follower
    def get(self, request, id1, format = None):
        pid = id1
        f = []
        for pid in PeopleFollowPeople.objects.filter(follower = id1):
            f.append(pid.followee)
        return Response(f)

def starFile(id, file): #idone star fileone or just cancel
    if PeopleStarFile.objects.filter(people = id, fileid = file):
        PeopleStarFile.objects.filter(people = id, fileid=file).delete()
        return False
    else:
        PeopleStarFile.objects.create(people=id, fileid=file)
        # JUMPING : WE CAN SEND A MESSAGE HERE
    return True

def getStarList(id): #get all the file stared
    f = []
    for file in PeopleStarFile.objects.filter(people = id):
        f.append(file)
    return f

def getAllStarer(file): #get all the id stared the file
    f = []
    for pid in PeopleStarFile.objects.filter(fileid = file):
        f.append(pid)
    return


class deleteComment(APIView):
    def delete(self, request, id, format = None):
        PeopleComment.objects.filter(commentid=id).delete()
        return Response(status=status.HTTP_200_OK)


class comment(APIView):
    #no permission check here ?
    permission_classes = (AllowAny,)
    def post(self, request, format = None):
        body = request.data
        t_userid = body['userID']
        t_fileid = body['fileID']
        t_date = body['date']
        t_type = body['type']
        if (t_type == "comment"): 
            t_comment = body['comment']
            if len(t_comment) > 200:
                return Response({"info":"Comment too long"},
                        status=status.HTTP_400_BAD_REQUEST)
            # JUMPING : WE CAN SEND A MESSAGE HERE
        if (t_type == "star"):
            pass
            # JUMPING : WE CAN SEND A MESSAGE HERE
        if (t_type == "score"):
            # JUMPING : WE CAN UPDATE FILE INFO HERE
            # JUMPING : WE CAN SEND A MESSAGE HERE
            pass
        t_commentid = random.randint(1, 2147483647)
        while (True):
           try:
               PeopleComment.objects.get(commentid = t_commentid)
               t_commentid = random.randint(1, 2147483647)
           except:
               break
        body['id'] = t_commentid
        _star = True if body.get('star') else False
        _score = body.get('score') if body.get('score') else 0
        _comment = body.get('comment') if body.get('comment') else ""
        PeopleComment.objects.create(commentid = t_commentid, userid = t_userid,
                                     fileid = t_fileid      , date = t_date,
                                     type = t_type          , comment = _comment,
                                     star = _star    , score = _score)
        return Response(body, status=status.HTTP_200_OK)

    def get(self, request, format = None):
        body = request.GET
        t_fileid = body['fileID']
        t_type = None
        try:
            t_type = body['type']
        except:
            t_type = None
        f = []
        for comment in PeopleComment.objects.filter(fileid = t_fileid):
            if (t_type == "" or comment.type == t_type):
                a_comment = {}
                a_comment['id'] = comment.commentid
                a_comment['userID'] = comment.userid
                a_comment['fileID'] = comment.fileid
                a_comment['date'] = comment.date
                a_comment['type'] = comment.type
                if comment.star == True:
                    a_comment['star'] = "true"
                else:
                    a_comment['star'] = "False"
                a_comment['score'] = comment.score
                a_comment['comment'] = comment.comment
                f.append(a_comment)
        return Response(f)
    
    def put(self,request,format=None):
        body = request.data
        print("raw id is %s"%body['id'])
        t_commentid = int(body['id'])
        print("id is %d"%t_commentid)
        _comment = PeopleComment.objects.get(commentid=t_commentid)
        _comment.fileid = body['fileID']
        _comment.userid = body['userID']
        _comment.date = body['date']
        _comment.type = body['type']
        if (body['star'] == True):
            _comment.star = True
        else:
            _comment.star = False
        _comment.score = body['score']
        _comment.comment = body['comment']
        _comment.save()
        return Response(body, status = status.HTTP_200_OK)

def removeFile(file): #remove the star and comment about a file
    PeopleStarFile.objects.filter(fileid = file).delete()
    PeopleComment.objects.filter(fileid = file).delete()
