
# Given an integer n, find the nth Fibonacci number Fn.
# 0 <= n <= 45

def fib(n):
	if n <= 1:
		return n
	current = 0
	next = 1

	for _ in range(2,n+1):
		current,next = next,current+next

	return next

if __name__ == "__main__" :
	print('Enter "n" to caculate fib(n)')
	n = int(input())
	print(fib(n))