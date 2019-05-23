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
    a = float(request.GET['a'])
    b = float(request.GET['b'])
    c = float(request.GET['c'])
    d = int(request.GET['d'])
    _payload = compute(a, b, c, d))
    _dict = {
        'temperature': a,
        'humidity': b,
        'concentration': c,
        'brightness': d
    }
    for i, j in _dict.items():
        r.set(i, j)
    return HttpResponse(_payload)
def compute(a, b, c, d):
    if int(r.get('npayload')) == 0:
        _payload = int(r.get('payload'))
        if standard('a', a, _payload) or standard(
                'b', b, _payload) or standard('c', c, _payload) or d == 0:
            return 1
        else:
            return 0
    else:
        return 1


def standard(key, value, _payload):
    if key == 'a':
        if float(value) > float(r.get('temperature')):
            if float(value) > 55:
                return 1
            else:
                return 0
        elif float(value) < float(r.get('temperature')):
            if float(value) > 45:
                return 1
            else:
                return 0
        else:
            return _payload
    if key == 'b':
        if float(value) > float(r.get('humidity')):
            if float(value) < 9:
                return 1
            else:
                return 0
        elif float(value) < float(r.get('humidity')):
            if float(value) < 11:
                return 1
            else:
                return 0
        else:
            return _payload
    if key == 'c':
        if float(value) > float(r.get('concentration')):
            if float(value) > 550:
                return 1
            else:
                return 0
        elif float(value) < float(r.get('concentration')):
            if float(value) > 450:
                return 1
            else:
                return 0
        else:
            return _payload
