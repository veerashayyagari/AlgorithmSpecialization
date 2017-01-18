#Uses python3

import sys

def isLarger_Or_Equal(num1,num2):
	if int(num2) <= 0:
		return True
	return (int(num1+num2) >= int(num2+num1))

def largest_number(digits):
    #write your code here
    res = ""
    while len(digits) > 0:
    	max_digit = str(-1)
    	for digit in digits:    		
    		if isLarger_Or_Equal(digit,max_digit):
    			max_digit = digit    	
    	del digits[digits.index(str(max_digit))]
    	res += max_digit
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]    
    print(largest_number(a))
    
