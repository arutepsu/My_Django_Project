import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse

from product.models import *
from product.forms import ProductForm, CategoryForm, ReviewForm


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


def product_create_view(requests):
    if requests.method == 'GET':
        context = {
            'form': ProductForm
        }
        return render(requests, 'products/create_product.html', context=context)
    if requests.method == 'PRODUCT':
        form = ProductForm(requests.PRODUCT, requests.FILES)

        if form.is_valid():
            Product.objects.create(**form.cleaned_data)

            return redirect('/products/')
        context = {
            'form': form,
        }
        return render(requests, 'products/create_product.html', context=context)


def category_create_view(requests):
    if requests.method == 'GET':
        context = {
            'form': CategoryForm
        }
        return render(requests, 'categories/create_category.html', context=context)
    if requests.method == 'CATEGORY':
        form = CategoryForm(requests.CATEGORY, requests.FILES)

        if form.is_valid():
            Product.objects.create(**form.cleaned_data)

            return redirect('/categories/')
        form.save()
        context = {
            'form': form,
        }
        return render(requests, 'categories/create_category.html', context=context)

def review_create_view(requests):
    if requests.method == 'GET':
        context = {
            'form': ReviewForm
        }
        return render(requests, 'products/detail.html', context=context)
    if requests.method == 'REVIEW':
        form = CategoryForm(requests.CATEGORY, requests.FILES)

        if form.is_valid():
            Product.objects.create(**form.cleaned_data)

            return redirect('/products/')
        context = {
            'form': form,
        }
        return render(requests, 'products/detail.html', context=context)
