# Uses python3
import sys
import random

def partition3(a, l, r):
    x = a[l]
    j = l
    k = 0

    for i in range(l+1,r+1):
        if a[i] < x :
            j = j + 1  
            
            # there is a possibility of swapping lower valued number into
            # equal valued number, first take care of moving that equal valued
            # number by swapping with a higher valued number
            if a[j] == x and a[j+k] > x:                
                a[j],a[j+k] = a[j+k],a[j]
            
            a[j],a[i] = a[i],a[j]

        elif a[i] == x :            
            k = k+1                        
            a[j+k],a[i] = a[i],a[j+k]

    a[l],a[j] = a[j],a[l]
    return (j,k)

def partition2(a, l, r):
    x = a[l]
    j = l;
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return

    k = random.randint(l, r)    
    #print("Input Array : {0}, Index: {1}, Value:{2}".format(a[l:r+1],k,a[k]))
    a[l], a[k] = a[k], a[l]
    #use partition3    
    (less,equal) = partition3(a, l, r) 
    #print("After Partition :{0}".format(a))   
    randomized_quick_sort(a, l, less - 1);
    randomized_quick_sort(a, less + equal + 1, r);


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
