#Uses python3

import sys

def explore(vertex,foundNode):
    if foundNode is True or visited[vertex] is True:
        return foundNode

    visited[vertex] = True

    for node in adj[vertex]:
        if visited[node] is False:
            if node == y:
                return True
            if(explore(node,foundNode)):
                return True
    return foundNode

def reach(adj, x, y):
    result = explore(x,False)
    return 1 if result is True else 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    visited = [False]*n
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    #print(adj)
    print(reach(adj, x, y))
