# Given two integers a and b, find the GCD

def gcd(a,b):
	if a == 0 or b == 0:
		return 0
	#if a > b swap
	if a > b:
		a,b = b,a

	#recursively mod b%a 
	while a > 0:
		a,b = b%a,a
	return b

if __name__ == "__main__":
	print('Enter the value of number "a" followed by space then number "b"')
	numbers = input()
	a,b = map(int,numbers.split())
	print(gcd(a,b))