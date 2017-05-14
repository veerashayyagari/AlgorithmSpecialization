#Uses python3

import sys
import queue
#import time





def distance(adj,cost, s, t):
    graph_length = len(adj)
    pq = queue.PriorityQueue()
    max_weight = graph_length * 1000
    dist = [max_weight for i in range(graph_length)]
    processed = [False for i in range(graph_length)]

    # set the distance for start
    dist[s] = 0

    # insert all the initial nodes with weights into pq
    for i in range(1,graph_length):
        pq.put((dist[i],i))

    # node to process initial value would be s
    node_to_process = (0,s)

    while node_to_process is not None:
        # if the node index is same as end index return
        if node_to_process[1] == t:
            return -1 if dist[t] == max_weight else dist[t]

        # if the node is already processed, ignore and continue
        if processed[node_to_process[1]] is True:
            node_to_process = None if pq.empty() is True else pq.get()
            continue

        # set the processed flag to True
        processed[node_to_process[1]] = True

        # iterate through all the connected edges and relax them if possible
        for idx,node in enumerate(adj[node_to_process[1]]):
            if processed[node] is False:
                weighted_distance = dist[node_to_process[1]] + cost[node_to_process[1]][idx]
                if weighted_distance < dist[node]:
                    dist[node] = weighted_distance
                    pq.put((weighted_distance,node))


        node_to_process = None if pq.empty() is True else pq.get()

    return -1 if dist[t] == max_weight else dist[t]




if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    #t1 = time.time()
    print(distance(adj,cost, s, t))
    #t2 = time.time()
    #print((t2 - t1)*1000)
