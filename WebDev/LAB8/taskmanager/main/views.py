from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Category


# Create your views here.


def products_list(request):
    products = Product.objects.all()
    return render(request, 'products_list/index.html', {'title': 'Products list', 'products': products})


def product(request ,id):
    products = Product.objects.all()
    for x in products:
        if x.id == id:
            return render(request, 'product/index.html', {'title': 'Product', 'product': x})
    return HttpResponse("<h1>Not found</h1>")


def categories_list(request):
    category = Category.objects.all()
    return render(request, 'products_list/index.html', {'title': 'Categories list', 'products': category})


def category(request ,id):
    category = Category.objects.all()
    for x in category:
        if x.id == id:
            return render(request, 'product/index.html', {'title': 'Category', 'category': x})
    return HttpResponse("<h1>Not found</h1>")