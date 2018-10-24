#!/usr/bin/python36 
# -*- coding:utf-8 -*-

import logging
from logging.handlers import TimedRotatingFileHandler

#日志系统， 既要把日志输出到控制台， 还要写入日志文件   
class Logger():
	def __init__(self, logname, loglevel, logger):
		'''
			指定保存日志的文件路径，日志级别，以及调用文件
			将日志存入到指定的文件中
		'''
        
        # 创建一个logger
		self.logger = logging.getLogger(logger)
		self.logger.setLevel(logging.DEBUG)
        
        # 创建一个handler，用于写入日志文件
        #fh = logging.FileHandler(logname,mode='w',encoding='UTF-8')
		fh = TimedRotatingFileHandler(logname,when = "D",interval = 1,backupCount = 30)

		fh.suffix = "%Y%m%d"
		fh.setLevel(logging.DEBUG)
        
        # 再创建一个handler，用于输出到控制台
		ch = logging.StreamHandler()
		ch.setLevel(logging.DEBUG)
        
        # 定义handler的输出格式
		formatter = logging.Formatter('%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s')
        #formatter = format_dict[int(loglevel)]
		fh.setFormatter(formatter)
		ch.setFormatter(formatter)
        
        # 给logger添加handler
		self.logger.addHandler(fh)
		self.logger.addHandler(ch)
        
    
	def getlog(self):
		return self.logger