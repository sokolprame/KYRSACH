from django.urls import path
from .views import home, register, login_view, logout_view  # Ensure these views exist in main/views.py

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
