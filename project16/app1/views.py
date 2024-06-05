from django.shortcuts import render

# Create your views here.
def text_list(request):
    course_list=["python","java","c","c++"]
    d={'list1':course_list}
    return render(request,'app1/res.html',context=d)