from django.shortcuts import render

# Create your views here.
import datetime
from django.http import HttpResponse

def display(request):
    dt=datetime.datetime.today()
    d=dt.date()
    h=dt.hour
    if h<=12:
        msg="<h1>Good Morning</h1>"
    elif h<=16:
        msg = "<h1>Good Morning</h1>"
    elif h<=24:
        msg = "<h1>Good Night</h1>"

    output=f'''<html>
    <body>
    <h1>current Date and Time is {dt}--> {msg}</h1>
    <a href="http://www.nareshit.com/">NARESHIT</a><br>
    </body>
    </html>'''
    return HttpResponse(output)
    
    
