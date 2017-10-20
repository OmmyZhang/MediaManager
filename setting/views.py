from django.shortcuts import render
from .models import Belong

# Create your views here.

def createBelong(ui,gi): # create a relationship between user and group 
    assert gi < 0 , "group id should < 0"
    b = Belong(user_id = ui , group_id = gi)
    b.save()

def checkBelong(ui,gi): # check if user belong to this group
    if Belong.objects.filter(user_id = ui , group_id = gi):
        return True
    else:
        return False

def groupMems(gi): # show all members in the group
    ui = []
    for bb in Belong.objects.filter(group_id = gi):
        ui.append(bb.user_id)
    return ui

def userGroups(ui):# show all groups that the user belong to
    gg = []
    for bb in Belong.objects.filter(user_id = ui):
        gg.append(bb.group_id)
    return gg




