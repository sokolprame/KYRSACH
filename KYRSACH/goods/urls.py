from django.urls import path
from django.contrib.auth import views as auth_views
from goods import views
import goods


app_name = 'goods'

urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('product/', views.catalog, name='product'),
]