#!/usr/bin/python
# coding=utf8
from functools import reduce
def max(L):
	return reduce(lambda x,y: x if x >= y else y, L)

num = [1,4,2,45,93]
print(max(num))



