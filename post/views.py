import datetime

from django.shortcuts import render
from django.http import HttpResponse


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
