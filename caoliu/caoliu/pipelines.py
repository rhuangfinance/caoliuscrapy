# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from caoliu import dbconn
import settings


class CaoliuPipeline(object):
    def process_item(self, item, spider):
        tdb = dbconn.Connection(
                    host = settings.DBHOST,
                    database = settings.DBBASE,
                    user = settings.DBUSER,
                    password = settings.DBPWD
                )

        item = self.check_data_exist(tdb, item)
        tdb.insert_by_dict(settings.DBTABLE, item, True)

        return item

    def check_data_exist(self, tdb, item):
        sql = "select id, created_at, parsed from {0} where url_md5=%s".format(settings.DBTABLE)
        url_md5 = item.get('url_md5')
        ret = tdb.get(sql, url_md5)

        if ret:
            id_ = ret.id
            created_at = ret.created_at
            parsed = ret.parsed
            item['id'] = id_
            item['created_at'] = created_at
            item['parsed'] = parsed

        return item
