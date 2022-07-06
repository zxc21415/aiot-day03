from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.http import JsonResponse
import datetime
def index(request):
    return HttpResponse("<h2>歡迎來到我的網站</h2>")

def date(request):
    return JsonResponse({'date':datetime.datetime.now()})