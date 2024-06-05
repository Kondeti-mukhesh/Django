from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def otp_view(request,name):
    otp=random.randint(1000,9999)
    output=f'''
<html>
<body>
<h1>Hello{name} and your otp is{otp}</h1>
</body>
<html>'''
    response=HttpResponse(output)
    return response