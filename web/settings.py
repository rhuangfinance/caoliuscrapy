#!/usr/bin/env python
#-*-coding:utf-8-*-
import os
settings = {
    "debug": True,
    "template_path": os.path.join(os.path.dirname(__file__), "templates"),
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "cookie_secret": "nvvFPjUTTxKh309Kb8V0opSxA8lLa0D6h0bN5Hd3L+s=",
    #"default_handler_class": ErrorPathHandler,
    "xsrf_cookies": True,
    "login_url": "/login",
    "gzip": True,
}

""" mysql 数据库配置 """
DBHOST = "localhost:3306"
DATABASE = "caoliu"
DBUSER = "root"
DBPWD = "c_p"
