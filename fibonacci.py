from sys import argv
def fib(max):
	n ,a ,b = 0, 0,1
	while n < max:
		print(n+1,b)
		a, b = b, a + b
		n += 1
	return 'done'

fib(int(argv[1]))
