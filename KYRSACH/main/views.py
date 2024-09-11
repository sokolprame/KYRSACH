from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterForm, LoginForm
from goods.models import Product

def index(request):
    new_products = Product.objects.filter(is_new=True)[:4]
    popular_products = Product.objects.filter(is_popular=True)[:4]
    discounted_products = Product.objects.filter(is_discounted=True)[:4]
    return render(request, 'main/index.html', {
        'new_products': new_products,
        'popular_products': popular_products,
        'discounted_products': discounted_products
    })

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main:index')
    else:
        form = RegisterForm()
    return render(request, 'main/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main:index')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'main/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('main:index')z