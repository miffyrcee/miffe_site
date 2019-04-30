#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 miffyrcee <miffyrcee@localhost.localdomain>
#
# Distributed under terms of the MIT license.
"""
format
"""
import json

vara = "tempature(C)"
varb = "humidity(RH%)"
varc = "concentration(PPM)"
vard = "vard"


def readJson(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
        return data
        f.close()


def writeJson(*args, **kwargs):
    data = json.dumps(kwargs)
    with open(args[0], 'w') as f:
        f.write(json.dumps(kwargs))
        f.close()
