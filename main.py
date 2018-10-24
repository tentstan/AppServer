#!/usr/bin/python36
#-*- coding:utf-8 -*-
#Author:tentstan
#Email:hailin8818@126.com
#version:1.0.0

import tornado.ioloop
import tornado.web
import os
import sys

from tornado.options import define,options
from common.url_router import include,url_wrapper
from models import initdb
from sqlalchemy.orm import scoped_session,sessionmaker
from conf.base import BaseDB,engine

class Application(tornado.web.Application):
    
    def __init__(self):

        initdb()
        handlers = url_wrapper([
            (r"/users/",include('views.users.users_urls'))
        ])

        settings = dict(
            debug = True,
            static_path = os.path.join(os.path.dirname(__file__),"static"),
            template_path = os.path.join(os.path.dirname(__file__),"templates")
        )
        tornado.web.Application.__init__(self,handlers,**settings)
        self.db = scoped_session(sessionmaker(bind=engine,
            autocommit=False,
            autoflush=True,
            expire_on_commit=False))


if __name__ == '__main__':
    print("Tornado server is ready for service\r")
    tornado.options.parse_command_line()
    Application().listen(8000,xheaders=True)
    tornado.ioloop.IOLoop.instance().start()
