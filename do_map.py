#!/usr/bin/python3
#coding=utf8

def f(x):
	return x * x

print(list(map(f,[x for x in range(1,11)])))
