from django.shortcuts import render

# Create your views here.
def text_view(request):
    name_list={'names':[{"name":"mukhesh","rollno":12,"course":"python"},
               {"name":"sanju","rollno":13,"course":"java"},]}
    return render(request,'app1/res.html',context=name_list)