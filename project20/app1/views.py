from django.shortcuts import render

# Create your views here.
def text_view(request,name,marks):
    c={'name':name,"marks":marks}
    return render(request,'app1/find.html',context=c)
   
