from django.shortcuts import render

# Create your views here.
def text_view(request):
    a=100 #local varibles
    b=200 #local varibles
    c=a+b
    d={'a':a,'b':b,'c':c}
    return render(request,'app1/results.html',context=d)