#/usr/bin/python3
# coding=utf8

import functools
import time

def log(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print('begin call')
		print('call %s():' % func.__name__)
		print('end call')
		return func(*args, **kw)
	return wrapper

@log
def print_now():
	print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


print_now()
print(print_now.__name__)

def logger(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print('%s %s():' % (text, func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator

@logger('DEBUG')
def today():
	print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

today()		
