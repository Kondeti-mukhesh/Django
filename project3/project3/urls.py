"""
URL configuration for project3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1.views import open_account as oa
from app1.views import close_account as ca
from app2.views import Home_loan as hl
urlpatterns = [
    path("open_account/",oa),
    path("close_account/",ca),
    path("Home_loan/",hl),
    path('admin/', admin.site.urls),
]
