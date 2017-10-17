from django.shortcuts import render
from .models import Belong

# Create your views here.

def createBelong(ui,gn): # create a relationship between user and group 
    b = Belong(user_id = ui , group_name = gn)
    b.save()

def checkBelong(ui,gn): # check if user belong to this group
    if Belong.objects.filter(user_id = ui , group_name = gn):
        return True
    else:
        return False

def groupMems(gn): # show all members in the group
    ui = []
    for bb in Belong.objects.filter(group_name = gn):
        ui.append(bb.user_id)
    return ui

def userGroups(ui):# show all groups that the user belong to
    gn = []
    for bb in Belong.objects.filter(user_id = ui):
        gn.append(bb.group_name)
    return gn




