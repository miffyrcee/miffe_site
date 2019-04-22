import json

import formaters
# Create your views here.
from bot import views as bv
from django.http import HttpResponse
from django.shortcuts import render


def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = request.GET['c']
    d = float(a) + float(b)
    formaters.writeJson('data.json', float(a), float(b), float(c))
    return HttpResponse(str(d))
