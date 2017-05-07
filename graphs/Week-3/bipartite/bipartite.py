#Uses python3

import sys
import queue

def bipartite(adj):
    graph_length = len(adj)
    q = queue.Queue()
    color = [-1 for _ in range(graph_length)]

    q.put(0)
    color[0] = 1

    while q.empty() is False:
        node_to_process = q.get()
        for node in adj[node_to_process]:
            if color[node] != -1 and color[node] == color[node_to_process]:
                return 0

            if color[node] == -1:
                color[node] = 1 - color[node_to_process]
                q.put(node)

    return 1


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
    print(bipartite(adj))
