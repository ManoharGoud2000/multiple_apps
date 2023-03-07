from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app2_first(request):
    return HttpResponse('<marquee><h1>This is 2nd App 1st funtion</marquee></h1>')


def app2_second(request):
    return HttpResponse('<marquee><h1>This is 2nd App 2nd funtion</marquee></h1>')
