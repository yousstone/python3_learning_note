from sys import argv
def odd():
	print('step 1')
	yield 1
	print('step 2')
	yield 2
	print('step 3')
	yield 3

o = odd()
s1 = next(o)
print(s1)
s2 = next(o)
print(s2)
s3 = next(o)
print(s3)


def fib(max):
	n ,a ,b = 0, 0,1
	while n < max:
		yield b                 
		a, b = b, a + b
		n += 1
	return 'done'
 
g = fib(int(argv[1]))
while True:
	try:
		x = next(g)
		print('g:',x)
	except StopIteration as e:
		print('Generator return value:', e.value)
		break
