from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    output='<h1>This is homepage</h1>'
    response=HttpResponse(output)
    return response

def index(request):
    output='<h1>This is index page</h1>'
    response=HttpResponse(output)
    return response

def content(request,value):
    output=f'<h1>value is {value}</h1>'
    response=HttpResponse(output)
    return response


