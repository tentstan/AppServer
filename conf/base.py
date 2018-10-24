#!/usr/bin/python36
# -*- coding:utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql://root@localhost:3306/demo?charset=utf8',encoding="utf8",echo=False)
BaseDB = declarative_base()

ERROR_CODE = {
    "0":"Success",
    "1001":"Invalid params",
    "1002":"user is registered, please login",
}