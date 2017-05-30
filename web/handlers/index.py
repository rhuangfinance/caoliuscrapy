#!/usr/bin/env python
#-*-coding:utf-8-*-
from base import BaseHandler
from tornado.web import authenticated

class IndexHandler(BaseHandler):
    @authenticated
    def get(self):
        sql = "select distinct(cat) as cat_id, cat_name as cat_desc from rawdata"
        ret = self.db.query(sql)
        self.render('index.html', datas=ret)
