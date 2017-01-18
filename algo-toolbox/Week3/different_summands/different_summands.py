# Uses python3
import sys

def optimal_summands(n):
    summands = []
    k = 1
    while True:
    	if n <= 2*k:
    		summands.append(n)
    		break;
    	else:
    		summands.append(k)    		
    		n = n-k
    		k = k+1

    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
