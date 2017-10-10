from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse

# Create your views here.
@login_required
def index(request):
    context = {
            "name":request.user.username
            }
    return HttpResponse("<h1>files here</h1> username: <b>"+request.user.username+"</b><br> <a href='/accounts/logout/'>logout</a>");

