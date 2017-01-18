# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    weight = 0.
    valueperweight = list(map(lambda x:x[0]/x[1],zip(values,weights)))    
    while (weight < capacity and len(valueperweight) > 0):
    	# find max valueperweight item index
    	idx = valueperweight.index(max(valueperweight))
    	# if item availability is less than or equal to available capacity, use it completely    	
    	availableCapacity = capacity - weight    	
    	if weights[idx] < availableCapacity:
    		weight += weights[idx]
    		value += values[idx]    		
    		del valueperweight[idx]
    		del values[idx]
    		del weights[idx]
    	else:
    		# use upto the remaining capacity and break    		
    		value += valueperweight[idx] * availableCapacity

    		break

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))
