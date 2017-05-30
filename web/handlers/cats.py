#!/usr/bin/env python
#-*-coding:utf-8-*-
from base import BaseHandler
from tornado.web import authenticated

class CatHandler(BaseHandler):
    @authenticated
    def get(self, cat_id):
        try:
            page = int(self.get_argument('page', 0))
        except Exception as e:
            page = 0
        try:
            size = int(self.get_argument('size', 300))
        except Exception as e:
            size = 300
        if size > 300:
            size = 300

        sql = "select * from rawdata where cat=%s order by publish_time desc limit %s, %s"
        ret = self.db.query(sql,
                                str(cat_id),
                                page*size,
                                size
                            )
        if not ret:
            next_page = page
        else:
            next_page = page + 1
        if page == 0:
            prev_page = 0
        else:
            prev_page = page - 1

        datas = {
            "datas": ret,
            "next_page": next_page,
            "prev_page": prev_page,
            "current_page": page,
            "cat_id": cat_id,
        }

        self.render('item.html', datas=datas)
