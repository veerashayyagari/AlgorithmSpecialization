# Uses python3
def edit_distance(s, t):
    s1_length = len(s)
    s2_length = len(t)

    dist = [[0 for _ in range(s1_length+1)] for _ in range(s2_length+1)]

    for i in range(s1_length+1):
    	dist[0][i] = i

    for j in range(s2_length+1):
    	dist[j][0] = j

    for i in range(1,s1_length+1):
    	for j in range(1,s2_length+1):
    		insertion_distance = dist[j-1][i] + 1
    		deletion_distance = dist[j][i-1] + 1
    		mismatch_distance = dist[j-1][i-1] + 1
    		match_distance = dist[j-1][i-1]

    		if s[i-1] == t[j-1]:
    			dist[j][i] = min(insertion_distance,deletion_distance,match_distance)
    		else:
    			dist[j][i] = min(insertion_distance,deletion_distance,mismatch_distance)

    return dist[s2_length][s1_length]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
