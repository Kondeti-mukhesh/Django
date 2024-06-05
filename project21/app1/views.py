from django.shortcuts import render

# Create your views here.
def text_view(request):
    sales_data={2000:20000,2001:40000,2003:45000,2004:60000}
    return render(request,'app1/res.html',context={'sales':sales_data})