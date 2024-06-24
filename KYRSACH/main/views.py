from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserRegisterForm

def index(request):
    return render(request, 'main/index.html')

def logout(request):
    auth_logout(request)
    return render(request, 'main/index.html') 

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = UserRegisterForm()
    return render(request, 'main/register/register.html', {'form': form})
