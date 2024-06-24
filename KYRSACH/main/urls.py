from lib2to3.pygram import pattern_grammar
from django.urls import include, path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect



urlpatterns = [
    path('', views.index),
    path('/catalog', include('goods.urls', namespace='catalog')),
    path('/accounts/', include('django.contrib.auth.urls')),
]
