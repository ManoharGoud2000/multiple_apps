from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app1_first(request):
    return HttpResponse('<marquee><h1> This is 1st App 1st function</marquee></h1>')
def app1_second(request):
        return HttpResponse('<marquee><h1> This is 1st App 2nd function</marquee></h1>')
