from django.shortcuts import render

# Create your views here.
def welcome(request):
    response=render(request,template_name='app1/welcome.html')
    return response
