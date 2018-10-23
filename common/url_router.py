#!/usr/bin/python36
#-*- coding:utf-8 -*-

from __future__ import unicode_literals
from importlib import import_module

def include(module):
    """according to the string pass in, call coresponding module,
    eg. is the module is register, call views.users_views.RegisterHansle module
    """
    res = import_module(module)
    urls = getattr(res,'urls',res)
    return urls

def url_wrapper(urls):
    """make the req url,call responding module,
    eg. make users,register into url/register 
    and call views.users.users_views.RegisterHandle module
    """
    wrapper_list = []
    for url in urls:
        path,handles = url
        if isinstance(handles,(tuple,list)):
            for handle in handles:
                pattern,handle_class = handle
                wrap = ('{0}{1}'.format(path,pattern),handle_class)
                wrapper_list.append(wrap)
        else:
            wrapper_list.append((path,handles))

    return wrapper_list
    
    