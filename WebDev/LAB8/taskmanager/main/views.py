from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Category
from django.http.response import JsonResponse


# Create your views here.


def products_list(request):
    try:
        product = Product.objects.all()
        products = [pro.to_json() for pro in product]
    except Product.DoesNotExist as e:
        return JsonResponse({'message': 'doesnt exist'})
    return JsonResponse(products, safe=False)


def product(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist as e:
        return JsonResponse({'message': 'doesnt exist'})
    return JsonResponse(product.to_json(), safe=False)


def categories_list(request):
    try:
        category = Category.objects.all()
        categories = [cat.to_json() for cat in category]
    except Product.DoesNotExist as e:
        return JsonResponse({'message': 'doesnt exist'})
    return JsonResponse(categories, safe=False)


def category(request ,id):
    try:
        category = Category.objects.get(id=id)
    except Product.DoesNotExist as e:
        return JsonResponse({'message': 'doesnt exist'})
    return JsonResponse(category.to_json(), safe=False)

