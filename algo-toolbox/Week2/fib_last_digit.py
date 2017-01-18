# Given an integer n, find the last digit of the nth fibonacci number

def fib_last_digit(n):
	# Identify the pattern that repeats for any given modulo. 
	# In this case mod10 and get the last digit with out calculating all the fibonacci numbers.
	if n <= 1:
		return n

	current = 0
	next = 1
	modlist = [0,1]
	for _ in range(2,n+1):
		current,next = next,current+next
		modlist.append(next%10)
		if next > 10 and modlist[-3:] == [0,1,1]:
			partitionLength = len(modlist) - 3
			rem = n%partitionLength
			return modlist[rem]

	return next%10

if __name__ == '__main__':
	print('Enter "n" to calculate the last digit of fib(n)')
	n = int(input())
	print(fib_last_digit(n))

		