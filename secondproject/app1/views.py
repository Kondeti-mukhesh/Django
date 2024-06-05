from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first(request):
    return HttpResponse("<h1>This is from first view</h1>")
def second(request):
    return HttpResponse("<h1>This is from second view</h1>")
def third(request):
    return HttpResponse("<h1>This is from third view</h1>")
