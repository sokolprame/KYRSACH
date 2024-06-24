"""
Definition of urls for KYRSACH.
"""

from datetime import datetime
from os import name
from django.urls import path
from django.contrib import admin
from django.urls import path, include 
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('/catalog', include('goods.urls', namespace='catalog'))
]
