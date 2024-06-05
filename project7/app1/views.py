from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def stud_adm(request):
    output="<h1>Student adm view</h1>"
    response=HttpResponse(output)
    return response

def stud_info(request):
    output="<h1>Student info view</h1>"
    response = HttpResponse(output)
    return response
