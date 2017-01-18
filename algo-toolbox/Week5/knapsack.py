# Uses python3
import sys

def optimal_weight(W, data):
	n = len(data)
	mapped_list = [[0 for _ in range(W+1)] for _ in range(n+1)]

	for (idx,val) in enumerate(data):
		for w in range(1,W+1):
			mapped_list[idx+1][w] = mapped_list[idx][w]
			if val <= w:
				optimal = mapped_list[idx][w-val] + val
				mapped_list[idx+1][w] = max(mapped_list[idx+1][w],optimal)
	return mapped_list[n][W] 


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *data = list(map(int, input.split()))
    print(optimal_weight(W, data))
