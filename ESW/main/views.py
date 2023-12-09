from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
    return HttpResponse("<h1>There we go</h1>")

def v1(response):
    return HttpResponse("<h1>CHA lala</h1>")
