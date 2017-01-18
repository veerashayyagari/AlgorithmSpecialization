# Uses python3
import sys

def merge(left_arr,right_arr,b,left):
    inversions_count = 0
    i = left
    while len(left_arr) > 0 and len(right_arr) > 0:
        if left_arr[0] <= right_arr[0]:
            b[i] = left_arr[0]
            i += 1
            del left_arr[0]
        else:
            b[i] = right_arr[0]
            i += 1
            inversions_count += len(left_arr)
            del right_arr[0]

    if len(left_arr) == 0 and len(right_arr) > 0:
        for a in right_arr:
            b[i] = a
            i += 1

    if len(right_arr) == 0 and len(left_arr) > 0:
        for a in left_arr:
            b[i] = a
            i += 1

    return inversions_count


def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        b[left] = a[left]
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    number_of_inversions += merge(b[left:ave],b[ave:right],b,left)
    return number_of_inversions

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)))
