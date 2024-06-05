from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def welcome(request):
    output="<h1>welcome to VS Code</h1>"
    response=HttpResponse
    return response(output)