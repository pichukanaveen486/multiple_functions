from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def string1(request):
    return HttpResponse('<h1>this is first string of app1</h1>')
