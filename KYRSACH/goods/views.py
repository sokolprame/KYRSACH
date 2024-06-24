from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from main.forms import PurchaseForm

def product_list(request):
    products = Product.objects.all()
    return render(request, 'goods/templates/main/catalog.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'goods/templates/main/purchase.html', {'product': product})

@login_required
def purchase(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.product = product
            order.save()
            return redirect('product_list')
    else:
        form = PurchaseForm()
    return render(request, 'goods/purchase.html', {'form': form, 'product': product})
