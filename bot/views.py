from django.http import HttpResponse
from django.shortcuts import render

from bot import views as bv

# Create your views here.

import json


def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = request.GET['c']
    d = int(a)+int(b)
    #  with f.open()

    return HttpResponse(str(d))
