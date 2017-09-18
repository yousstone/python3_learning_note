#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
	def __init__(self, name, score):
		self.__name = name
		self.__score = score
	def get_name(self):
		return self.__name

	def get_score(self):
		return self.__score

	def set_name(self, name):
		self.__name = name

	def set_score(self, score):
		if 0 <= score <= 100:
			self.__score = score
		else:
			print('Not bewteen 0 and 100, Bad socre')

	def get_grade(self):
		if self.__score >= '90':
			return '优秀'
		elif self.__scroe >= 60:
			return '良好'
		else:
			return '不及格'

bart = Student('Bart Simpson', 59)
print('bart.get_name()=', bart.get_name())
bart.set_score(60)
print('bart.get_score()=',bart.get_score())

print('DO NOT use bart._Stuendt__name:', bart._Student__name)	


