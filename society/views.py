# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import PeopleFollowPeople, PeopleStarFile, PeopleComment
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
#More import if needed


def followSb(APIView):   #idone follow idtwo or just cancel
    #followee follow the follower, this is not halal
    def post(self, request, format = None):
        body = request.data
        idone = body['id']
        idtwo = body['othersID']
        #if PeopleFollowPeople.objects.filter(followee = idone, follower = idtwo):
        #No need to check this if frontend is correct
        PeopleFollowPeople.objects.create(followee = idone, follower = idtwo)
        return Response(status=status.HTTP_200_OK)
    def delete(self, request, format = None):
        body = request.data
        idone = body['id']
        idtwo = body['othersID']
        PeopleFollowPeople.objects.filter(followee = idone, follower = idtwo).delete()
        return Response(status=status.HTTP_200_OK)
    else:

        # JUMPING : WE CAN SEND A MESSAGE HERE
    return True

def getFollowerList(APIView):
    def get(self, request, format = None):
        body = request.data
        pid = body['id']
        f = []
        for pid in PeopleFollowPeople.objects.filter(followee = id):
            f.append(pid.follower)
        return Response(f)

def getFolloweeList(APIView): # get all the follower
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

def deleteComment(APIView):
    def delete(self, request, format = None):
        body = request.data
        cid = body['id']
    #About comment, we need to rewrite

def commentDealer(APIView):
    #no permission check here ?
    #wait to finish
    #not halal yet
    def post(self, request, format = None):
        body = request.data
        id = body['userid']
        file = body['fileid']
        comment = body['comment']
        if len(comment) > 200:
            return Response({"info":"Comment too long"},
                    status=status.HTTP_400_BAD_REQUEST)
        PeopleComment.objects.create(people=id, fileid=file, comment=comment)
        # JUMPING : WE CAN SEND A MESSAGE HERE
        return Response(status=status.HTTP_200_OK)

    def get(self, request, format = None):
        body = request.data
        f = []
        for comment in PeopleComment.objects.filter(fileid=file):
            infotuple = (comment.id, comment.comment)
            f.append(infotuple)
            #This is not halal
        return f

def removeFile(file): #remove the star and comment about a file
    PeopleStarFile.objects.filter(fileid = file).delete()
    PeopleComment.objects.filter(fileid = file).delete()
