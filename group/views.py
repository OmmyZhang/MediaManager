from django.shortcuts import render
from .models import Belong
from files.models import StTag
from files.views import new_tag,get_tag
from rest_framework import status,permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAdminUser

# Create your views here.




class TheGroup(APIView):
    permission_classes = (IsAdminUser,)

    def get(self, request, format=None):
        return Response([{
            'id':g.id,
            'name':g.name
            }
            for g in StTag.objects.filter(isGroup = True)
            ])

    def post(self, request, format=None):
        body = request.data
        id = new_tag(body['name'], True)
        return Response({
            'id':id,
            'name':body['name']
            })
  

class GroupById(APIView):

    def get(self, request, id, format=None):
        g = get_tag(id)
        if (g is not None) and  g.isGroup:
            return Response({
                'id':g.id,
                'name':g.name
                })
        else:
            return Response({'info':'Wrong id'},
                    status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id ,format=None):
        g = get_tag(id)
        body = request.data
        if (g is not None) and  g.isGroup:
            g.name = body['name'] 
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'info':'Wrong id'},
                    status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id ,format=None):
        g = get_tag(id)
        body = request.data
        if (g is not None) and  g.isGroup:
            g.delete()
            Belong.objects.filter(group_id=id).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'info':'Wrong id'},
                    status=status.HTTP_400_BAD_REQUEST)


#-------------------------------------------
def create_Belong(ui,gi): # create a relationship between user and group
    b = Belong(user_id = ui , group_id = gi)
    b.save()

def check_Belong(ui,gi): # check if user belong to this group
    if Belong.objects.filter(user_id = ui , group_id = gi):
        return True
    else:
        return False

def group_mems(gi): # show all members in the group
    ui = []
    for bb in Belong.objects.filter(group_id = gi):
        ui.append(bb.user_id)
    return ui

def user_groups(ui):# show all groups that the user belong to
    gg = []
    for bb in Belong.objects.filter(user_id = ui):
        gg.append(bb.group_id)
    return gg




