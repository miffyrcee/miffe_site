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
    d = readJson('data.json')["vard"]
    formaters.writeJson('data.json', float(a), float(b), float(c), float(d))
    return HttpResponse(str(d))
