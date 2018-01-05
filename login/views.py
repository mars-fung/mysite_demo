from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def AllIndex(request):
    return HttpResponse("全网站的index页面")

def index(request):
    return HttpResponse("这个APP：login的index页面")