# Given an integer 𝑛,  nd the last digit of the sum 𝐹0 +𝐹1 +···+𝐹𝑛.

def fib_sum_last_digit(n):
	# sum(fib(n)) == fib(n+2) - 1,
	# last digit is mod 10 of fib(n+2), for mod 10 pattern length = 60,
	# calculate last digit of fib(n+2%60) - 1
	if n <= 1:
		return n

	rem = (n+2)%60
	current = 0
	next = 1
	for _ in range(2,rem+1):
		current,next = next,current+next

	last_digit = next%10
	return 9 if last_digit == 0 else (last_digit - 1)

if __name__ == "__main__":
	print("Enter the number 'n' to calculate the sum and last digit")
	n = int(input())
	print(fib_sum_last_digit(n))