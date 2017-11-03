# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import PeopleFollowPeople, PeopleStarFile, PeopleComment

def followSb(idone, idtwo):   #idone follow idtwo or just cancel
    #followee follow the follower, this is not halal
    if PeopleFollowPeople.object.filter(followee = idone, follower = idtwo):
        PeopleFollowPeople.object.filter(followee = idone, follower = idtwo).delete()
        return False
    else:
        PeopleFollowPeople.object.create(followee = idone, follower = idtwo)
        # JUMPING : WE CAN SEND A MESSAGE HERE
    return True

def getFollowerList(id): #get all the people this id followed
    f = []
    for id in PeopleFollowPeople.object.filter(followee = id):
        f.append(id.follower)
    return f

def getFolloweeList(id): # get all the follower
    f = []
    for id in PeopleFollowPeople.object.filter(follower = id):
        f.append(id.followee)
    return f

def starFile(id, file): #idone star fileone or just cancel
    if PeopleStarFile.object.filter(people = id, fileid = file):
        PeopleStarFile.object.filter(people=id, fileid=file).delete()
        return False
    else:
        PeopleStarFile.object.create(people=id, fileid=file)
        # JUMPING : WE CAN SEND A MESSAGE HERE
    return True

def getStarList(id): #get all the file stared
    f = []
    for file in PeopleStarFile.object.filter(people = id):
        f.append(file)
    return f

def getAllStarer(file): #get all the id stared the file
    f = []
    for id in PeopleStarFile.object.filter(fileid = file):
        f.append(id)
    return

def postComment(id, file, comment): #id post a comment about file
    if (len(comment) > 200):
        return False
    #Send ERROR HERE
    PeopleComment.object.create(people = id, fileid = file, comment = comment)
    # JUMPING : WE CAN SEND A MESSAGE HERE
    return True

def getComment(file): #get all comment about that tile
    f = []
    for comment in PeopleComment.object.filter(fileid = file):
        infotuple = (comment.id, comment.comment)
        f.append(infotuple)
    return f

def removeFile(file): #remove the star and comment about a file
    PeopleStarFile.object.filter(fileid = file).delete()
    PeopleComment.object.filter(fileid = file).delete()
    return True
