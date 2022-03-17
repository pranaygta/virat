from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def rcb(request):
    return HttpResponse('<marquee><h1>virat king</h1></marquee>')
