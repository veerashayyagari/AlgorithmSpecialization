#Uses python3
import sys
import math

def distance(p1,p2):
    x = (p2[0] - p1[0])**2
    y = (p2[1] - p1[1])**2
    return round(math.sqrt(x+y),10)

def find(p,pointIndexDict,parents):
    p_idx = pointIndexDict[str(p)]
    parent_idx = parents[p_idx]

    while parent_idx != parents[parent_idx]:
        parent_idx = parents[parent_idx]

    # Union by Rank Heuristic, move the node up to the parent
    parents[p_idx] = parent_idx 
    return parent_idx

def clustering(x, y, k):
    distances = []
    ranks = []
    parents = []
    pointIndexDict = {}

    for i in range(n):
        ranks.append(1)
        parents.append(i)
        t1 = (x[i],y[i])
        pointIndexDict[str(t1)] = i
        for j in range(i+1,n):
            t2 = (x[j],y[j])
            distances.append((distance(t1,t2),(t1,t2)))

    distances = sorted(distances,key=lambda x:x[0])

    # No.Of times the merge occurs determines the number of children and parents
    # For node count of 12, if merge occurs 9 times which means there are 9 children
    # and 3 parents, grouped as 3 clusters. Next time merge occurs whatever min distance
    # present is the value of d
    merge_counter = 0

    for d,(p1,p2) in distances:
        pointer_p1 = find(p1,pointIndexDict,parents)
        pointer_p2 = find(p2,pointIndexDict,parents)

        if pointer_p1 != pointer_p2:
            rank_p1 = ranks[pointer_p1]
            rank_p2 = ranks[pointer_p2]
            if rank_p1 > rank_p2:
                parents[pointer_p2] = pointer_p1
                ranks[pointer_p1] += ranks[pointer_p2]
            else:
                parents[pointer_p1] = pointer_p2
                ranks[pointer_p2] += ranks[pointer_p1]
            merge_counter += 1

            if merge_counter > (n - k) :
                return d




if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k)))
