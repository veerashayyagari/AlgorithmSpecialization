#Uses python3
import sys
import math
import time

def distance(p1,p2):
	x = (p2[0] - p1[0])**2
	y = (p2[1] - p1[1])**2
	return round(math.sqrt(x+y),10)

def find(p1,pointIndexDict,parents):
	idx_p1 = pointIndexDict[str(p1)]
	parent_idx = parents[idx_p1]

	# for parent it will be it's own index
	# while we reach the parent we iterate up
	while parent_idx != parents[parent_idx]:
		parent_idx = parents[parent_idx]

	# Rank by Union Heurisitc, where we move the node being searched to the parent
	parents[idx_p1] = parent_idx
	return parent_idx

def minimum_distance(x, y):
    result = 0.
    distances = []
    parents = []
    ranks = []
    pointIndexDict = {}

    # find all distances    
    for i in range(n):
    	#initialize rank to 1    	
    	ranks.append(1)
    	# initialize each to be parent of it's own
    	parents.append(i)

    	t1 = (x[i],y[i])
    	# insert indexes for each point to associate with parents and ranks
    	pointIndexDict[str(t1)] = i    	

    	for j in range(i+1,n):
    		t2 = (x[j],y[j])
    		distances.append((distance(t1,t2),(t1,t2)))


    # sort distances , ascending of distance
    distances = sorted(distances,key=lambda x:x[0])

    for d,(p1,p2) in distances:
    	pointer_p1 = find(p1,pointIndexDict,parents)
    	pointer_p2 = find(p2,pointIndexDict,parents)

    	#flag to identify the max nodes have reached
    	isFinal = False

    	# while both the sets are disjoint, try to merge them
    	if pointer_p1 != pointer_p2:
    		rank_p1 = ranks[pointer_p1]
    		rank_p2 = ranks[pointer_p2]

    		if rank_p1 > rank_p2:
    			# parent of p2 should p1
    			parents[pointer_p2] = pointer_p1

    			#ranks of p1 should be incremented by rank of p2
    			ranks[pointer_p1] += ranks[pointer_p2]

    			if ranks[pointer_p1] == n:
    				isFinal = True

    		else:
    			parents[pointer_p1] = pointer_p2
    			ranks[pointer_p2] += ranks[pointer_p1]

    			if ranks[pointer_p2] == n:
    				isFinal = True
    		result += d

    	if isFinal == True:
    		break

    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    t1 = time.time()
    print("{0:.9f}".format(minimum_distance(x, y)))
