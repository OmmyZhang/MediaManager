# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import PeopleFollowPeople, PeopleStarFile, PeopleComment
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
import random
import remainder.views
#More import if needed


class followSb(APIView):   #idone follow idtwo or just cancel
    #followee follow the follower, this is not halal
    def post(self, request, format = None):
        print("--------------------------------$$$$$$$$$$$$$$$$$$$$$$$$$test")
        body = request.data
        idone = body['id']
        idtwo = body['othersID']
        #if PeopleFollowPeople.objects.filter(followee = idone, follower = idtwo):
        #No need to check this if frontend is correct
        PeopleFollowPeople.objects.create(followee = idone, follower = idtwo)
        remainder.views.sentNotice(idtwo,  str(idone) + 'has followed you! ');
        return Response(status=status.HTTP_200_OK)
    def delete(self, request, format = None):
        body = request.data
        idone = body['id']
        idtwo = body['othersID']
        PeopleFollowPeople.objects.filter(followee = idone, follower = idtwo).delete()
        return Response(status=status.HTTP_200_OK)
        # JUMPING : WE CAN SEND A MESSAGE HERE

class getFollowerList(APIView):
    def get(self, request, format = None):
        body = request.data
        pid = body['id']
        f = []
        for pid in PeopleFollowPeople.objects.filter(followee = id):
            f.append(pid.follower)
        return Response(f)

class getFolloweeList(APIView): # get all the follower
    def get(self, request, format = None):
        body = request.data
        pid = body['id']
        f = []
        for pid in PeopleFollowPeople.objects.filter(followee = id):
            f.append(pid.follower)
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
    def delete(self, request, format = None):
        body = request.data
        t_commentid = body['commentid']
        PeopleComment.objects.filter(commentid=t_commentid).delete()
        return Response(status=status.HTTP_200_OK)


class commentDealer(APIView):
    #no permission check here ?
    def post(self, request, format = None):
        body = request.data
        t_uesrid = body['userId']
        t_fileid = body['fileId']
        t_date = body['date']
        t_type = int(body['type'])
        if (t_type == 1):
            t_comment = body['comment']
            if len(t_comment) > 200:
                return Response({"info":"Comment too long"},
                        status=status.HTTP_400_BAD_REQUEST)
            # JUMPING : WE CAN SEND A MESSAGE HERE
        if (t_type == 2):
            pass
            # JUMPING : WE CAN SEND A MESSAGE HERE
        if (t_type == 3):
            # JUMPING : WE CAN UPDATE FILE INFO HERE
            # JUMPING : WE CAN SEND A MESSAGE HERE
            pass
        t_commentid = random.randint(1, 2147483647)
        while (True):
            if PeopleComment.objects.filter(commentid = t_commentid):
                break
            t_commentid = random.randint(1, 2147483647)
        PeopleComment.objects.create(commentid = t_commentid, userid = t_userid,
                                     fileid = t_fileid      , date = t_date,
                                     type = t_type          , comment = body['comment'],
                                     star = body['star']    , score = body['score'])
        return Response(status=status.HTTP_200_OK)

    def get(self, request, format = None):
        body = request.data
        t_fileid = body['fileId']
        t_type = body['type']
        f = []
        for comment in PeopleComment.objects.filter(fileid = t_fileid, type = t_type):
            a_comment = {}
            a_comment['commentid'] = comment.commentid
            a_comment['userid'] = comment.userid
            a_comment['fileid'] = comment.fileid
            a_comment['date'] = comment.date
            a_comment['type'] = comment.type
            a_comment['star'] = comment.star
            a_comment['score'] = comment.score
            a_comment['comment'] = comment.comment
            f.append(a_comment)
        return Response(f)

def removeFile(file): #remove the star and comment about a file
    PeopleStarFile.objects.filter(fileid = file).delete()
    PeopleComment.objects.filter(fileid = file).delete()
