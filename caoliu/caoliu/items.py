# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class CaoliuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    cat = scrapy.Field()
    cat_name = scrapy.Field()
    url = scrapy.Field()
    url_md5 = scrapy.Field()
    title = scrapy.Field()
    publish_time = scrapy.Field()
    content = scrapy.Field()
    created_at = scrapy.Field()
    parsed = scrapy.Field()
