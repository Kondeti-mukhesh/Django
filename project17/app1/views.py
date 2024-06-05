from django.shortcuts import render

# Create your views here.
class employee:
    def __init__(self):
        self.empno=12
        self.ename="mukhesh"
        self.salary=25000

def table_view(request):
    emp=employee()
    c={'e':emp}
    return render(request,'app1/result.html',context=c)


