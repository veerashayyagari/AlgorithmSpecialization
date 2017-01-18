# Uses python3
import sys

def get_majority_element(a,left,right):
    # if an element is present more than n/2 times
    # if we increment the count everytime we find the same element
    # decrement everytime we find a different element
    # by the end of the scan it finds the candidate element    
    if left > right:
        return -1

    if left == right:
        return a[left]
    
    max_element_index = 0
    count = 1

    for i in range(1,len(a)):        
        if a[i] == a[max_element_index]:
            count += 1
        else:
            count -= 1           

        if count == 0:
            count = 1
            max_element_index = i

    count = 0
    for i in a:
        if a[max_element_index] == i:
            count += 1
            if count > len(a)/2 :
                return count

    return -1


def count(a,left,right,value):
    i = 0
    for v in range(left,right+1):
        if a[v] == value:
            i += 1

    return i


def get_majority_element_divide_and_conquer(a,left,right):

    if left > right:
        return -1

    if left == right:
        return a[left]

    mid = left + (right-left)//2

    left_count = get_majority_element_divide_and_conquer(a,left,mid)
    right_count = get_majority_element_divide_and_conquer(a,mid+1,right)

    if left_count != -1 and right_count == -1 :        
        num = count(a,left,right,left_count)        
        if (num > (right-left + 1)/2):
            return left_count
        else:
            return -1
    elif left_count == -1 and right_count != -1 :
        num = count(a, left,right,right_count)        
        if num > ((right - left + 1)/2):
            return right_count
        else:
            return -1

    elif left_count != -1 and right_count != -1 :
        left_num = count(a,left,right,left_count)        
        if left_num > (right-left+1)/2 :
            return left_count

        right_num = count(a,left,right,right_count)        
        if right_num > (right-left+1)/2 :
            return right_count

        return -1
    else:
        return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))    
    if get_majority_element_divide_and_conquer(a, 0, n-1) != -1:
        print(1)
    else:
        print(0)
