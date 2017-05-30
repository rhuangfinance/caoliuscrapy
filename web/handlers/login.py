#!/usr/bin/env python
#-*-coding:utf-8-*-
from base import BaseHandler

class LoginHandler(BaseHandler):
    def get(self):
        self.render('login.html')

    def post(self):
        self.set_secure_cookie("username", self.get_argument("username"))
        self.redirect("/")
