# Given two integers n and m,output Fib(n) mod m
# 1≤𝑛≤10^18,2≤𝑚≤10^5.

def fib_huge_mod(n,m):
	#find the pattern which repeats for mod m
	current = 0
	next = 1
	modlist = [0,1]
	for _ in range(2,n+1):
		current,next = next,current+next
		modlist.append(next%m)
		if next > m and modlist[-3:] == [0,1,1]:
			patternLength = len(modlist) - 3
			rem = n%patternLength
			return modlist[rem]

	return next%m

if __name__ == "__main__":
	print("Enter number 'n' to calculate Fib(n) followed by space then number 'm' that denotes the modulo")
	numbers = input()
	a,b = map(int,numbers.split())
	print(fib_huge_mod(a,b))
