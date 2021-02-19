import random

from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from .models import Category, Product


def search(request):
    query = request.GET.get('query', '')
    products = Product.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))

    return render(request, 'product/search.html', {'products': products, 'query': query})

def product(request, category_slug, product_slug):
    display_product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)

    similar_products = list(display_product.category.products.exclude(id=display_product.id))

    if len(similar_products) >= 4:
        similar_products = random.sample(similar_products, 4)
    
    return render(request, 'product/product.html', {'display_product': display_product, 'similar_products': similar_products})
    
def category(request, category_slug):
    categories = get_object_or_404(Category, slug=category_slug)

    return render(request, 'product/category.html', {'categories': categories})