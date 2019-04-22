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


def writeJson(file_path, a, b, c, d):
    data = {vara: a, varb: b, varc: c, vard: d}
    with open(file_path, 'w') as f:
        json.dump(data, f)
        f.close()
