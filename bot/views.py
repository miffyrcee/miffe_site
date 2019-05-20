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
    return HttpResponse(int(r.get(payload)))


def compute(a, b, c, d):

    if (a > standrad('temperature', a, 50)) or (b < hStandrad(
            'humidity', b, 10)) or (c > standrad('concentration', c, 500)) or (
                d > standrad('brightness', d, 700)):
        r.set('payload', 1)
    else:
        r.set('payload', 0)

    _dict = {
        'temperature': a,
        'humidity': b,
        'concentration': c,
        'brightness': d
    }
    for i, j in _dict.items():
        r.set(i, j)


def standrad(key, value, standardLine):
    _value = r.get(str(key))
    if (value - float(_value) > 0):
        return standrad * 1.1
    else:
        return standrad * 0.9


def hStandrad(key, value, standardLine):
    _value = r.get(str(key))
    if (value > float(_value)):
        return standrad * 0.9
    else:
        return standrad * 1.1
