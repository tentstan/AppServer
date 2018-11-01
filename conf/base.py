#!/usr/bin/python36
# -*- coding:utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql://root@localhost:3306/demo?charset=utf8',encoding="utf8",echo=False)
BaseDB = declarative_base()

SERVER_HEADER = "http://172.13.0.59:8000"

ERROR_CODE = {
    "0":"Success",
    "1001":"Invalid params",
    "1002":"user is registered, please login",
    "1003":"user has not been registered,please register",
    "2001":"image upload can not be empty"
}