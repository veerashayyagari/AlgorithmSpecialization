#Uses python3

import sys
from collections import deque
#import time

def relax_edges(edge1,edge2,dist,weight):
    weighted_distance = dist[edge1] + weight
    if dist[edge2] > weighted_distance:
        dist[edge2] = weighted_distance
        return True
    return False


def find_distances(graph,cost,processed,start):
    graph_length = len(graph)
    max_weight = graph_length*1000
    dist = [max_weight for _ in range(graph_length)]
    dist[start] = 0
    q = deque([start])    
    iteration = 0

    while len(q) > 0:                
        iteration += 1

        # if it is the graph length iteration, return 1
        if iteration > graph_length or dist[start] < 0:
            return 1

        node_to_process = q.pop()
        processed[node_to_process] = True

        for idx,node in enumerate(graph[node_to_process]):
            if relax_edges(node_to_process,node,dist,cost[node_to_process][idx]):
                q.append(node)
    return 0



def negative_cycle(adj, cost):
    
    graph_length = len(adj)
    processed = [False for _ in range(graph_length)]

    # foreach node in the graph as start, relax the edges
    for i in range(len(adj)):
        if processed[i] is False and find_distances(adj,cost,processed,i) == 1:
            return 1

    return 0


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
    #t1 = time.time()
    print(negative_cycle(adj, cost))
    #t2 = time.time()
    #print((t2 - t1)*1000)
