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


def product_detail_view(request, product_id):
    if request.method == 'GET':
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return render(request, '404.html')

        context = {
            'products': product,
        }

        return render(
            request,
            'products/detail.html',
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
            'categories/list.html',
            context=context
        )


def review_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()

        context = {
            'reviews': reviews,
        }

        return render(request,
                      'reviews/review_list.html',
                      context=context)
