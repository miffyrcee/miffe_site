import re

import redis
# Create your views here.
from bot import views as bv
from django.http import HttpResponse
from django.shortcuts import render

pool = redis.ConnectionPool(host='149.129.115.88',
                            port=6379,
                            db=0,
                            password='foobared')
r = redis.Redis(connection_pool=pool)


def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = request.GET['c']
    d = request.GET['d']
    compute(a, b, c, d)
    return HttpResponse(int(r.get('payload')))


def compute(a, b, c, d):
    if int(r.get('npayload')) == 0:
        if float(a) > float(r.get('temperature')) and float(a) > 55:
            _payload = 1
        elif float(a) < float(r.get('temperature')) and float(a) > 45:
            _payload = 1
        elif float(a) == float(r.get('temperature')) and int(r.get('payload')):
            _payload = 1
        else:
            if float(b) > float(r.get('humidity')) and float(b) < 9:
                _payload = 1
            elif float(b) < float(r.get('humidity')) and float(a) < 11:
                _payload = 1
            elif float(a) == float(r.get('humidity')) and int(
                    r.get('payload')):
                _payload = 1
            else:
                if float(c) > float(r.get('concentration')) and float(b) > 550:
                    _payload = 1
                elif float(b) < float(
                        r.get('concentration')) and float(a) > 450:
                    _payload = 1
                elif float(a) == float(r.get('concentration')) and int(
                        r.get('payload')):
                    _payload = 1
                else:
                    r.set('payload', 0)

    else:
        r.set('payload', 1)

    _dict = {
        'temperature': a,
        'humidity': b,
        'concentration': c,
        'brightness': d
    }
    for i, j in _dict.items():
        r.set(i, j)
