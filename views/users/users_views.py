#! /usr/bin/python36
#-*- coding:utf-8 -*-

import tornado.web
from tornado.escape import json_decode
from datetime import datetime

import common.logger
from common.logger import Logger

from common.commons import(
    http_response,
)

from conf.base import(
    ERROR_CODE,
)


from models import(
    Users)

log = Logger(logname='log/users/users.log', loglevel=1, logger="users").getlog()

class RegisterHandle(tornado.web.RequestHandler):
    """handle /users/register request
    param phone:user sign up phone
    param password:user sign up password
    param code:user sign up code,must six digital code
    """

    @property
    def db(self):
        return self.application.db

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
        
        ex_user = self.db.query(Users).filter_by(phone=phone).first()
        if ex_user:
            http_response(self,ERROR_CODE['1002'],1002)
            self.db.close()
            return
        else:
            log.debug("RegisterHandle: insert db,user:%s" %(phone))
            create_time = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
            add_user = Users(phone,password,create_time)
            self.db.add(add_user)
            self.db.commit()
            self.db.close()

            log.debug("RegisterHandle: register Success!")
            http_response(self,ERROR_CODE['0'],0)


class LoginHandle(tornado.web.RequestHandler):
    """ handle /users/login request
        param phone: user sign up phone
        param password:user sign up password
    """
    @property 
    def db(self):
        return self.application.db

    def get(self):
        try:
            phone = self.get_argument("phone")
            password = self.get_argument("password")
        except:
            log.info("LoginHandle:request argument incorrect")
            http_response(self,ERROR_CODE['1001'],1001)
            return

        ex_user = self.db.query(Users).filter_by(phone=phone).first()
        if ex_user:
            log.debug("LoginHandle: get user login,%s" %(phone))
            self.render("index.html")
            self.db.close()
            return
        else:
            http_response(self,ERROR_CODE['1003'],1003)
            self.db.close()
            return