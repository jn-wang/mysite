from django.contrib import admin
from django.urls import path
from XB import views

urlpatterns = [
    path('', views.XB),
    path('single', views.single),
    path('movies', views.movies ),
    path('music', views.music ),
    path('addVideo', views.addVideo ),
]