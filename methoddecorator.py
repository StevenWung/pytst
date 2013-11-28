#-*- coding: utf-8 -*-


class AE2BaseException(Exception):
	def test(self):
		pass
class AE2Exception(AE2BaseException):
	def __init__(self, msg):
		self.msg=msg
		pass
	def __str__(self):
		return self.msg


def trys(fn):
	def try_call(*args, **kwargs):
		try:
			print 'in trys'
			return fn(*args, **kwargs)
		except KeyError, e:
			raise AE2Exception('key: {0} not found'.format(e))
		except ZeroDivisionError, e:
			raise AE2Exception('0 cannot be devided by 0')
		except Exception, e:
			print 'afasfdasdf'
			#raise AE2Exception('shit')
	return try_call

class A(object):
	def __init__(self):
		self.init()
	def init(self):
		print 'init in parent'
    	pass

class B(A):
    def init(self):
    	print 'init in child'
    	pass

@trys
def test():

		a = {'a':1}
		print a['a']
try:
	test()
	x = "asdfaf" + 1
except AE2BaseException, e:
	print e