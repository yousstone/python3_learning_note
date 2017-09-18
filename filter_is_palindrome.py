#!/usr/bin/python3
# coding=utf8

def is_palindrome(n):
	str_n = str(n)
	if str_n == str_n[::-1]:
		return True
	else:
		return False

output = list(filter(is_palindrome, range(1,1000)))
print(output)
