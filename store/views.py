from django.db.models import query
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render
from .models import Category, Product  
from django.db.models import Q

def product_all (request):
    products = Product.objects.filter(is_active=True)
    return render(request, 'store/home.html', {'products': products})


def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/products/category.html', {'category': category, 'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/products/single.html', {'product': product})


def about(request):
    return render(request, "store/about.html")


def contact(request):
    return render(request, "store/contact.html")
    

def search(request):
    Q = request.GET.get('Q', '') 
    QuerySet= (Q(title_nombre_icontains=Q)) | (Q(description_nombre_icontains=Q))
    products = Product.objects.filter(QuerySet)
    return render(request, 'store/search.html', {'products': products})
