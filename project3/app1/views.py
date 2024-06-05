from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def open_account(request):
    output='''<html>
    <body>
    <h1>welcome to HDFC bank</h1>
    </body>
    </html>'''
    response=HttpResponse(output)
    return response

def close_account(request):
    output='''<html>
    <body>
    <h1>Thanks for using service of HDFC</h1>
    </body>
    </html>'''
    response = HttpResponse(output)
    return response
