from django.http import HttpResponse
from django.shortcuts import render

def func3(request):
    return HttpResponse('Hello')
def func4(request):
    return HttpResponse('How are you?')
def func5(request):
    return HttpResponse('it is a good day')


