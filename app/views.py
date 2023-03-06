from django.shortcuts import render
from django.http import HttpResponse
def amiya(request):
    return HttpResponse('<h1>My name is Amiya</h1>')
def abc(request):
    return HttpResponse('<h1>my name is abc</h1>')

# Create your views here.
