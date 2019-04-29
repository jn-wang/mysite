"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.urls import path,include,re_path
from Dome import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    re_path(r'^pay/', views.pay),
    re_path(r'^pay_result/', views.pay_result),
    re_path(r'^updata_order/', views.updata_order),
    path('XB/', include('XB.urls')),
    path('resume/', views.resume),
    path('file/', views.file_down),
    path('hbdl/', views.hbdl),
    path('img/', views.img),
    path('calculate/', views.calculate),
    path('search/', views.search,name='search'),
]
