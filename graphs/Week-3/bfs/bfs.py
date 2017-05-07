#Uses python3

import sys
import queue

def distance(adj, s, t):
    graph_length = len(adj)
    distance = [-1 for _ in range(graph_length)]
    q = queue.Queue()
    q.put(s)
    distance[s] = 0

    while q.empty() is False:
        node_to_process = q.get()

        if(node_to_process == t):
            return distance[node_to_process]

        for node in adj[node_to_process]:
            if distance[node] == -1:
                q.put(node)
                distance[node] = distance[node_to_process] + 1

    return distance[t]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
