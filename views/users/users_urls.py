#!/usr/bin/python36
#-*- coding:utf-8 -*-

from __future__ import unicode_literals
from .users_views import (
    RegisterHandle
)

urls = [
    (r'register',RegisterHandle)
]