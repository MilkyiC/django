from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('Здравствуйте')
def func1(request):
    return HttpResponse('Как дела?')
def func2(request):
    return HttpResponse('Сегодня хорошая погода')


