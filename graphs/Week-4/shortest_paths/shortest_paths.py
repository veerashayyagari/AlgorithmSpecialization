#Uses python3

import sys
#import time
from collections import deque


def dfs(graph,cost,start,prev):
    graph_length = len(graph)
    q = deque([start])
    visited = [False for _ in range(graph_length)]
    relaxed_nodes = deque()

    while len(q) > 0:
        node_to_process = q.popleft()

        if visited[node_to_process] is False:
            visited[node_to_process] = True
            for idx,node in enumerate(graph[node_to_process]):
                q.append(node)
                reachable[node] = 1
                weighted_distance = distance[node_to_process] + cost[node_to_process][idx]
                if weighted_distance < distance[node]:
                    distance[node] = weighted_distance
                    relaxed_nodes.append(node)   
                    prev[node] = node_to_process                 
    return relaxed_nodes


def update_negative_cycle(graph,edge):
    q = deque([edge])
    shortest[edge] = 0
    visited = [False for _ in range(len(graph))]

    while len(q) > 0:
        node_to_process = q.popleft()

        if visited[node_to_process] is False:
            visited[node_to_process] = True
            for node in graph[node_to_process]:
                q.append(node)
                shortest[node] = 0




def shortet_paths(adj, cost, s, distance, reachable, shortest):
    graph_length = len(adj)
    distance[s] = 0
    reachable[s] = 1  
    prev = [None for _ in range(graph_length)]  

    for i in range(1,graph_length+1):
        negative_cycle = dfs(adj,cost,s,prev)
        if len(negative_cycle) == 0:
            break

    while len(negative_cycle) > 0:
        cycle_node = negative_cycle.popleft()
        if shortest[cycle_node] != 0:
            update_negative_cycle(adj,cycle_node)
    




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
    s = data[0]
    s -= 1
    distance = [float("inf")] * n
    reachable = [0] * n
    shortest = [1] * n
    #t1 = time.time()
    shortet_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])
    #t2 = time.time()
    #print((t2-t1)*1000)

