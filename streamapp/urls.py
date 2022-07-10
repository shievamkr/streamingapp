from django.contrib import admin
from django.urls import path
from streamapp import views

urlpatterns = [

    path('', views.Home, name='home')
]
