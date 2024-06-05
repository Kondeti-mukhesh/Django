from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    output="<h1>This is index view</h1>"
    response=HttpResponse(output)
    return response

def home(request):
    output ="<h1>This is home view</h1>"
    response = HttpResponse(output)

    return response
def welcome(request,name):
    output = f'<h1>{name}hello welcome</h1>'
    response = HttpResponse(output)
    return response



