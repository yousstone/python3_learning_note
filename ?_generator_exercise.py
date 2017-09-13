# coding=utf8
# 没有实现杨辉三角这题，题在生成器的最后
from sys import argv
def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield b
		a ,b = b ,a+b
		n += 1
	return 'done'

def triangles1(max):
	n = 1
	while n <= max:
		print([x for x in fib(n)])
		n += 1

def triangles2():
	n, a, b = 0, 0, 1
