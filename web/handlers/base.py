#!/usr/bin/env python
#-*-coding:utf-8-*-
""" base handler for all other handlers """
import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    def __init__(self, application, request, **kwargs):
        super(BaseHandler, self).__init__(application, request, **kwargs)

    @property
    def db(self):
        return self.application.db

    @property
    def geo(self):
        return self.application.es

    def get_current_user(self):
        user = self.get_secure_cookie('username')

        return user if user == 'daixiepython.com' else None
