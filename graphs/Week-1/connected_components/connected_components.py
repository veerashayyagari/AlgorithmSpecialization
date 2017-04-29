#Uses python3

import sys

def explore(vertex):
    visited[vertex] = True

    for node in adj[vertex]:
        if visited[node] is False:
            explore(node)


def number_of_components(adj):
    result = 0
    
    for i in range(n):
        if visited[i] is False:
            result += 1
            explore(i)
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    visited = [False]*n
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))
