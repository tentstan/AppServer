#! /usr/bin/python36
#-*- coding:utf-8 -*-

import tornado.web
from tornado.escape import json_decode

import common.logger

from common.commons import(
    http_response,
)

from conf.base import(
    ERROR_CODE,
)

log = Logger.Logger().getlog(logname='log.txt', loglevel=1, logger="fox")

class RegisterHandle(tornado.web.RequestHandler):
    """handle /users/register request
    param phone:user sign up phone
    param password:user sign up password
    param code:user sign up code,must six digital code
    """

    def post(self):
        try:
            args = json_decode(self.request.body)
            phone = args['phone']
            password = args['password']
            verify_code = args['code']
        except:
            log.info("RegisterHandle: request argument incorrect!")
            http_response(self,ERROR_CODE['1001'],1001)
            return
        
        log.debug("RegisterHandle: register Success!")
        http_response(self,ERROR_CODE['0'],0)