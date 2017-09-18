#/usr/bin/python3
# coding=utf8

# 可变参数

def calc(*numbers):
	sum = 0
	for n in numbers:
		sum += n*n
	return sum

print(calc())
print(calc(*[1,2,3]))
print(calc(*range(1,11)))
print(calc(1,3,5))
