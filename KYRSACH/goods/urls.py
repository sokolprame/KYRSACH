from django.urls import path
from django.contrib.auth import views as auth_views
from goods import views



urlpatterns = [
    path('', views.catalog, name='index'),
    path('product/', views.catalog, name='product'),
]