#! /usr/bin/python36
# -*- coding:utf-8 -*-

#upload_views.py

import tornado.web
import os
from tornado.escape import json_decode
import json

import common.logger
from common.logger import Logger

from common.commons import(
    http_response,
    save_files
)

from conf.base import(
    ERROR_CODE,
    SERVER_HEADER
)

SAVE_IMAGE_PATH = "static/image/"

log = Logger(logname='log/upload/upload.log', loglevel=1, logger="upload").getlog()

class UploadFileHandle(tornado.web.RequestHandler):
	""" handle /upload/file request,upload image and save it to static/image
	param: image,upload image
	"""	

	def post(self):
		try:
			image_metas = self.request.files['image']
		except:
			log.info("UploadFileHandle: request argument incorrect!")
			http_response(self,ERROR_CODE['1001'],1001)
			return	

		image_url = ""
		image_path_list = []

		if image_metas:
			pwd = os.getcwd()
			save_image_path = os.path.join(pwd,SAVE_IMAGE_PATH)
			log.debug("UploadFileHandle: save image path:%s" %(save_image_path))
			file_name_list = save_files(image_metas,save_image_path)
			image_path_list = [SERVER_HEADER + save_image_path + i for i in file_name_list] 
			ret_data = {"imageUrl": image_path_list}
			self.write(json.dumps({"data":{"msg":ret_data,"code":0}}))
		else:
			log.info("UploadFileHandle: image stream is empty")
			http_response(self,ERROR_CODE['2001'],2001)
