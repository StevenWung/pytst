#-*- coding: utf-8 -*-
import tornado.ioloop
import tornado.web


class TestWebA(tornado.web.RequestHandler):
	def get(self):
		self.write('shit a')

class TestWebB(tornado.web.RequestHandler):
	def get(self):
		self.write('shit b')

applicationa = tornado.web.Application([
	('/a', TestWebA)
])
applicationa.listen(19090)

applicationb = tornado.web.Application([
	('/b', TestWebB)
])
applicationb.listen(19091)

tornado.ioloop.IOLoop.instance().start()