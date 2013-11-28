#-*- coding: utf-8 -*-
import tornado.ioloop
import tornado.web


class TestWeb(tornado.web.RequestHandler):
    def get(self):
        self.write('shit')

application = tornado.web.Application([
    ('/a', TestWeb)
])
application.listen(19090)
tornado.ioloop.IOLoop.instance().start()