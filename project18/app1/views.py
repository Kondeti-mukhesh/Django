from django.shortcuts import render

# Create your views here.
def text_view(request):
    stud_data={'name':"mukhesh",
               "rollno":12,
               "course":"python",}
    c={'student':stud_data}
    return render(request,'app1/res.html',context=c)
