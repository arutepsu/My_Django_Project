import datetime

from django.shortcuts import render
from django.http import HttpResponse

from product.models import *


def hello_view(request):
    if request.method == 'GET':
        return HttpResponse("Hello! It's my Django project")


def current_date(request):
    if request.method == 'GET':
        current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return HttpResponse(current_date)


def bye_view(request):
    if request.method == 'GET':
        return HttpResponse("Bye User!")


def l_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')


def main_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')


def product_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        context = {
            'products': products,
        }
        return render(
            request,
            'products/products.html',
            context=context
        )


def categories_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()

        context = {
            'categories': categories,
        }

        return render(
            request,
            'products/products.html',
            context=context
        )
