from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Home_loan(request):
    output='''<html>
    <body>
    <h1>welcome to HDFC bank
    </body>
    </html>'''
    response=HttpResponse(output)
    return response


