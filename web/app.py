#!/usr/bin/env python
# -*-coding:utf-8-*-
import tornado.web
from tornado.web import URLSpec
import tornado.httpserver
import tornado.options
from tornado.options import define, options
import tornado.ioloop
import dbconn as torndb
import settings
from handlers import *

define("port", default=9876, type=int, help="使用端口, --port=9876")


class App(tornado.web.Application):
    def __init__(self):
        handlers = [
            URLSpec(r'/', IndexHandler),
            URLSpec(r'/cat/(\d{1,2})', CatHandler, name="cat"),
            URLSpec(r'/detail/(\w+)', DetailHandler),
            URLSpec(r'/login', LoginHandler),
        ]

        tornado.web.Application.__init__(self, handlers, **settings.settings)
        self.db = torndb.Connection(host=settings.DBHOST, database=settings.DATABASE, user=settings.DBUSER, password=settings.DBPWD)

def main():
    tornado.options.parse_command_line()
    app = App()
    server = tornado.httpserver.HTTPServer(app, xheaders=True)
    server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
