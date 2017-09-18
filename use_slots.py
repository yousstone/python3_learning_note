
from types import MethodType
class Student(object):
	pass

s = Student()
s.name = 'Michael'
print(s.name)

def set_age(self, age):
	self.age = age

s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)

s1 = Student()
s1.set_age(35)
