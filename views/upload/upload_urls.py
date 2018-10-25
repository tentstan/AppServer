#! /usr/bin/python36
# -*- coding:utf-8 -*-

#upload_urls.py

from __future__ import unicode_literals
from .upload_views import (
	UploadFileHandle)

urls = [
	(r'file',UploadFileHandle)
]
