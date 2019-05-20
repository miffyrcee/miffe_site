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

    if (float(a) > standrad('temperature', a, 50)) or (float(b) < hStandrad(
            'humidity', b, 10)) or (float(c) > standrad(
                'concentration', c, 500)) or (float(d) > standrad(
                    'brightness', d, 700)):
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
    if (float(value) - float(_value) > 0):
        return standardLine * 1.1
    else:
        return standardLine * 0.9


def hStandrad(key, value, standardLine):
    _value = r.get(str(key))
    if (float(value) > float(_value)):
        return standardLine * 0.9
    else:
        return standardLine * 1.1
