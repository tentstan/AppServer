#! /usr/bin/python36
#-*- coding:utf-8 -*-

import tornado.web
from tornado.escape import json_decode

from common.commons import(
    http_response,
)

from conf.base import(
    ERROR_CODE,
)

class RegisterHandle(tornado.web.RequestHandler):
    '''handle /users/register request
    param phone:user sign up phone
    param password:user sign up password
    param code:user sign up code,must six digital code
    '''

    def post(self):
        try:
            args = json_decode(self.request.body)
            phone = args['phone']
            password = args['password']
            verify_code = args['code']
        except:
            http_response(self,ERROR_CODE['1001'],1001)
            return
        
        http_response(self,ERROR['0'],0)