# Given two integers a,b calculate least common multiple
# Obviously LCM * GCD = a * b

def gcd(a,b):
	if a > b:
		a,b = b,a

	while a > 0:
		a,b = b%a,a
	return b

def lcm(a,b):
	divisor = gcd(a,b)
	return (a*b)//divisor

if __name__ == "__main__":
	print("Enter number 'a' followed by space then number 'b' to calculate lcm")
	numbers = input()
	a,b = map(int,numbers.split())
	print(lcm(a,b))
