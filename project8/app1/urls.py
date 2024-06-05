from django.urls import path
from . import views
urlpatterns =[
    path("adm/",views.stud_adm),
    path("info/",views.stud_info)
]