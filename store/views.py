from django.shortcuts import get_object_or_404, render, redirect
from .models import Category, Product  
from django.db.models import Q
from django.db.models import query
from django import forms
from .forms import *
from django.contrib import messages

product = Product.objects.all()

productWhithImage= []
productWhithoutImage= []
for i in range(10):
    if (i <= 2):
        productWhithImage.append(product[i])
    else:
        productWhithoutImage.append(product[i])

def product_all (request):
    list_productimage = Product.objects.all().order_by("-id")[:3]
    list_productSinimage = Product.objects.all().order_by("-id")[3:10]

    def get(self, request, *args, **kwargs):
            return render (request, self.template_name, {"self.list_productimage": list_productimage, "self.list_productSinimage": list_productSinimage})
    
    return render(request, 'store/home.html', {
            "list_productimage": productWhithImage,
            "list_productSinimage": productWhithoutImage,
        })


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
    query=None
    results=[]
    if request.method == "GET":
        query = request.GET.get('search')
        results = Product.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
        return render(request, 'store/search.html', {'query': query, 'results':results})
    else:
        return render(request, 'store/search.html')
      

def new_product(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto creado con exito')
            return redirect('store:new_product') 
    else:       
        form = ArticuloForm()
    return render(
        request=request,
        template_name='store/new_product.html',
        context={'agregar': form})


def edition_product(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        form = UpdateArticuloForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/')         
    else:
        form = UpdateArticuloForm(instance=product)
        return render(request, 'store/edition_product.html'), {'product': product, 'form': form }

def delete_product_db(request, product_id):
    product= Product.objects.get(id=product_id)
    product.delete()
    messages.succes(request, 'Producto eliminado')
    return redirect('home')

