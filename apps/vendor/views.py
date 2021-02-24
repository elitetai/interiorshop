from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.utils.text import slugify
from django.shortcuts import render, redirect

from .models import Vendor
from apps.product.models import Product

from .forms import ProductForm

def become_vendor(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST) # A ModelForm for creating a new user

        if form.is_valid(): # checks for any unfilled fields
            user = form.save()
            login(request, user)

            vendor = Vendor.objects.create(name=user.username, created_by=user)
            return redirect('core:frontpage')

    else: 
        form = UserCreationForm()

    return render(request, 'vendor/become_vendor.html', {'form': form})

@login_required
def vendor_admin(request):
    vendor = request.user.vendor # HttpRequest.user falls under AuthenticationMiddleware
    products = vendor.products.all()
    orders = vendor.orders.all()

    for order in orders:
        order.vendor_amount = 0 
        order.vendor_paid_amount = 0
        order.fully_paid = True

        for item in order.items.all():
            if item.vendor == request.user.vendor:
                if item.vendor_paid:  # Would need to manually set it to True
                    order.vendor_paid_amount += item.get_total_price() # Not pass in/save yet?
                else:
                    order.vendor_amount += item.get_total_price()
                    order.fully_paid = False

    data = {
        'vendor': vendor, 
        'products': products, 
        'orders': orders
    }

    return render(request, 'vendor/vendor_admin.html', data)

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            product = form.save(commit=False) # created, but don't save the new form instance yet
            product.vendor = request.user.vendor
            product.slug = slugify(product.title)
            product.save()

            return redirect('vendor:vendor_admin')
    else: 
        form = ProductForm()
        
    return render(request, 'vendor/add_product.html', {'form': form})

@login_required
def edit_vendor(request):
    vendor = request.user.vendor

    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')

        if name:
            vendor.created_by.email = email
            vendor.created_by.save()

            vendor.name = name
            vendor.save()

            return redirect('vendor:vendor_admin')

    return render(request, 'vendor/edit_vendor.html', {'vendor': vendor})