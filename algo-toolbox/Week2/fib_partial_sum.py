#Given two non-negative integers 𝑚 and 𝑛, where 𝑚 ≤ 𝑛,  nd the last digit of the sum 𝐹𝑚 + 𝐹𝑚+1 + ···+𝐹𝑛.

def fib_partial_sum(m,n):
	if m == n:
		# then it's last digit of fib(m) which is last digit of fib(m%60)
		rem = m%60
		current = 0
		next = 1
		for _ in range(2,rem+1):
			current,next = next,current+next
		return next%10

	# sum(fib(n)) - sum(fib(m-1)) == fib(n+2)%60 - fib(m+1)%60
	remN = (n+2)%60
	remM = (m+1)%60

	current = 0
	next = 1
	for _ in range(2,remN+1):
		current,next = next, current+next

	last_digitN = next%10

	current = 0
	next = 1
	for _ in range(2,remM+1):
		current,next = next,current+next

	last_digitM = next%10

	if(last_digitN >= last_digitM) :
		return (last_digitN - last_digitM)
	else:
		return (last_digitN - last_digitM + 10)


if __name__ == "__main__":
	print("type the smaller number 'm' followed by space then larger name 'n' for calculating partial sum")
	numbers = input()
	m,n = map(int,numbers.split())
	print(fib_partial_sum(m,n))