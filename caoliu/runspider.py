#!/usr/bin/env python
#-*-coding:utf-8-*-
import argparse
import time
#import logging

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
#from scrapy.utils.log import configure_logging

from caoliu.spiders.caoliu_spider import CaoLiuSpider

#logging.basicConfig(
    #filename='/tmp/caoliu.log',
    #format='%(name)s %(levelname)s %(asctime)s: %(message)s',
    #datefmt="%Y-%m-%d %H:%M:%S",
    #level=logging.DEBUG
#)
#configure_logging({'LOG_STDOUT': True})

def run(max_page=5):
    settings = get_project_settings()
    settings.set('MAX_PAGE', max_page, 'project')
    crawler_process = CrawlerProcess(settings)
    crawler_process.crawl(CaoLiuSpider)
    crawler_process.start()

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--maxpage', default=20, type=int)
    parser.add_argument('--sleep', default=300, type=int)
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_args()
    max_page = args.maxpage
    sleep_time = args.sleep
    run(max_page)
