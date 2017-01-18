# Uses python3
import sys

def points_counter(sorted_list):
    counter = 0
    points_dict = {}
    for l in sorted_list:
        if l[1] == 'f':
            counter += 1
        elif l[1] == 'e':
            counter -= 1
        else:
            points_dict[l[0]] = counter
    return points_dict


def merge(first,last):
    sorted_list = []

    while len(first) > 0 and len(last) > 0:
        if first[0][0] < last[0][0]:
            sorted_list.append(first[0])
            del first[0]
        elif first[0][0] == last[0][0] and ((first[0][1] == 'p' and last[0][1] == 'e') or (first[0][1] == 'f' and last[0][1] == 'p') or (first[0][1] == 'f' and last[0][1] == 'e')):
            sorted_list.append(first[0])
            del first[0]
        else:
            sorted_list.append(last[0])
            del last[0]

    if len(first) == 0 and len(last) > 0:
        sorted_list += last
    elif len(last) == 0 and len(first) > 0:
        sorted_list += first

    return sorted_list


def merge_sort(list_to_sort):
    if len(list_to_sort) <= 1:
        return list_to_sort
    ave = len(list_to_sort)//2
    first_half = merge_sort(list_to_sort[0:ave])
    second_half = merge_sort(list_to_sort[ave:len(list_to_sort)])
    return merge(first_half,second_half)

def naive_count_segments(starts, ends, points):
    starts_tuple = list(map(lambda x:(x,'f'),starts))
    ends_tuple = list(map(lambda x:(x,'e'),ends))
    points_tuple = list(map(lambda x:(x,'p'),points))
    list_to_sort = starts_tuple + ends_tuple + points_tuple    
    sorted_list = merge_sort(list_to_sort)
    points_count = points_counter(sorted_list)
    return points_count

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = naive_count_segments(starts, ends, points)
    for x in points:
        print(cnt[x], end=' ')
