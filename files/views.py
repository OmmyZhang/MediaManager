from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse

# Create your views here.
@login_required
def index(request):
    return HttpResponse("<h1>files here</h1>");

