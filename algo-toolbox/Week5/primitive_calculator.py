# Uses python3
import sys
import math

def prepare_list(n):    
    opscount = [0]*(n+1)
    opscount[2] = 1
    opscount[3] = 1

    for i in range(4,n+1):
        by_3 = float('inf')
        by_2 = float('inf')
        by_1 = float('inf')

        if i%3 == 0:
            by_3 = opscount[i//3] + 1

        if i%2 == 0:
            by_2 = opscount[i//2] + 1

        by_1 = opscount[i-1] + 1
        opscount[i] = min(by_1,by_2,by_3)

    return opscount



def optimal_sequence(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1,2]
    if n == 3:
        return [1,3]

    opscount = prepare_list(n)
    optimal_count = opscount[n]
    sequence = [0]*(optimal_count + 1)
    sequence[0] = 1
    sequence[optimal_count] = n
    counter = optimal_count - 1
    while n > 1:
        by_3 = float('inf')
        by_2 = float('inf')
        by_1 = float('inf')

        if n%3 == 0:            
            by_3 = opscount[n//3] + 1

        if n%2 == 0:
            by_2 = opscount[n//2] + 1

        by_1 = opscount[n-1] + 1

        minimum = min(by_1,by_2,by_3)

        if minimum == by_3:
            n = n//3
        elif minimum == by_2:
            n = n//2
        else:
            n = n-1

        sequence[counter] = n
        counter -= 1
    return sequence


input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
