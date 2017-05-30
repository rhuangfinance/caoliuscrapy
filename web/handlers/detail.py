#!/usr/bin/env python
#-*-coding:utf-8-*-
from base import BaseHandler

class DetailHandler(BaseHandler):
    def get(self, url_md5):
        sql = "select * from rawdata where url_md5=%s"
        ret = self.db.get(sql, url_md5)
        self.render('detail.html', data=ret)

def test():
    pass

if __name__ == "__main__":
    test()

