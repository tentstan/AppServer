#! /usr/bin/python36
# -*- coding:utf-8 -*-

import json

def http_reponse(self,msg,code):
    self.write(json.dumps({"data":{"msg":msg,"code":code}}))

if __name__ == "__main__":
    http_reponse()
