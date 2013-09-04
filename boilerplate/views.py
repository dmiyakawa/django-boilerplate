# -*- coding=utf-8 -*-

from __future__ import print_function

import os.path
from os.path import dirname

from django.shortcuts import render

NAMESPACE = os.path.basename(dirname(dirname(os.path.abspath(__file__))))

def home(request):
    return render(request, '{}/home.html'.format(NAMESPACE),
                  {'message': 'hello',
                   'is_secure': request.is_secure() })
