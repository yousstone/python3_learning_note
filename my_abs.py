#/usr/bin/python3
# coding=utf8
import sys

def my_abs(x):
	if not isinstance(x ,(int,float)):
		raise TypeError('Bad operand type')
	if x >= 0:
		return x
	else:
		return -x

print(my_abs(int(sys.argv[1])))
