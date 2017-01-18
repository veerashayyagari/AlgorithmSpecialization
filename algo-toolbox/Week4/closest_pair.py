# Uses python3
import sys
import math

def merge(first,second,idx):
	merged_list = []
	while len(first) > 0 and len(second) > 0 :
		if first[0][idx] <= second[0][idx]:
			merged_list.append(first[0])
			del first[0]
		else:
			merged_list.append(second[0])
			del second[0]
	if len(first) == 0 and len(second) > 0:
		merged_list += second
	elif len(second) == 0 and len(first) > 0:
		merged_list += first

	return merged_list

def merge_sort(list_to_sort,idx):
	if len(list_to_sort) <= 1:
		return list_to_sort

	ave = len(list_to_sort)//2
	first_half = merge_sort(list_to_sort[0:ave],idx)
	second_half = merge_sort(list_to_sort[ave:len(list_to_sort)],idx)
	return merge(first_half,second_half,idx)

def brute_force_min_distance(points):
	min_dist = float('inf')
	for i in range(0,len(points)):
		for j in range(i+1,len(points)):
			p1 = points[i]
			p2 = points[j]
			dist = math.pow(p2[0]-p1[0],2) + math.pow(p2[1]-p1[1],2)
			if dist < min_dist:
				min_dist = dist

	return round(math.sqrt(min_dist),6)

def filter_list_x_less_than_min_dist(sorted_by_x,min_dist):
	filtered_list = []
	ave = len(sorted_by_x)//2
	mid = sorted_by_x[ave]
	filtered_list.append(mid)
	for i in range(0,ave):
		if  mid[0] - sorted_by_x[i][0] < min_dist:
			filtered_list.append(sorted_by_x[i])

	for i in range(ave+1,len(sorted_by_x)):
		if sorted_by_x[i][0] - mid[0] < min_dist:
			filtered_list.append(sorted_by_x[i])

	return filtered_list

def divide_and_conquer_min_distance(points):
	if len(points) <= 3 :
		return brute_force_min_distance(points)

	ave = len(points)//2
	left_points_min = divide_and_conquer_min_distance(points[0:ave])
	#print("LEFT MIN -> {0} for LIST -> {1}".format(left_points_min,points[0:ave]))
	right_points_min = divide_and_conquer_min_distance(points[ave:len(points)])
	#print("RIGHT MIN -> {0} for LIST -> {1}".format(right_points_min,points[ave:len(points)]))
	#print("LEFT -> {0}, RIGHT -> {1}".format(left_points_min,right_points_min))
	min_dist = min(left_points_min,right_points_min)
	# filter the list to consider points that are at maximum min_dist on x axis from median	
	#print("Min Distance -> {0}".format(min_dist))
	filtered_list = filter_list_x_less_than_min_dist(points,min_dist)
	# sort this filtered list by 'y' axis
	sorted_by_y = merge_sort(filtered_list,1)
	#print("Sorted_By_Y -> {0}, Min_Dist -> {1}".format(sorted_by_y,min_dist))	

	# maximum of 6 iterations to compare among - http://www.geeksforgeeks.org/closest-pair-of-points/
	for i in range(0,len(sorted_by_y)):
		j = i + 1			
		while j < len(sorted_by_y) and (sorted_by_y[j][1] - sorted_by_y[i][1]) < min_dist:
			p1 = sorted_by_y[j]
			p2 = sorted_by_y[i]
			dist = round(math.sqrt(math.pow(p2[0]-p1[0],2) + math.pow(p2[1]-p1[1],2)),6)
			if dist < min_dist:
				min_dist = dist		
			j += 1

	return min_dist


def find_min_distance(firsts,ends):
	data_list = list(zip(firsts,ends))
	#print("Input Data -> {0}".format(data_list))
	# sort by x using merge sort
	sorted_by_x = merge_sort(data_list,0)
	#print("Sorted on X -> {0}".format(sorted_by_x))
	# use divide and conquer to identify min on either side of median
	return divide_and_conquer_min_distance(sorted_by_x)	
	


if __name__ == "__main__":
	input = sys.stdin.read()
	data = list(map(int,input.split()))
	n = data[0]
	firsts = data[1:2*n+1:2]
	ends = data[2:2*n+1:2]
	print(find_min_distance(firsts,ends))