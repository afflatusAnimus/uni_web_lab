from django.http import HttpResponse
from django.shortcuts import render
from django import template

# def home(request):
#     return HttpResponse(u'Привет, Мир!', content_type="text/plain; charset=utf-8")

def home(request):
    return render(request, 'templates/static_handler.html')

