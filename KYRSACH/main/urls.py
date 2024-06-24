from django.contrib.auth import login
from django.urls import path
from .views import index, register, login, logout

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('login/', login, name='login'), 
    path('logout/', logout, name='logout'),
]
