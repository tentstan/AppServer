#! /usr/bin/python36
# -*- coding:utf-8 -*-

from conf.base import BaseDB,engine
import sys
from sqlalchemy import(
	Column,
	Integer,
	String,
	DateTime)

class Users(BaseDB):
	"""table for users
	"""

	__tablename__ = "users"

	id = Column(Integer,primary_key=True)
	phone = Column(String(50),nullable=False)
	password = Column(String(50),nullable=True)
	createTime = Column(DateTime,nullable=True)

	def __init__(self,phone,password,createTime):
		self.phone = phone
		self.password = password
		self.createTime = createTime

def initdb():
	BaseDB.metadata.create_all(engine)

if __name__ == '__main__':
	print("Initialize database")
	initdb()

		
