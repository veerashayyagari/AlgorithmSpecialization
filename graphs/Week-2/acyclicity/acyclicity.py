#Uses python3

import sys

def explore(root,vertex,hascycle):
    if hascycle is True:
        return True

    visited[vertex] = True

    for node in adj[vertex]:
        if node == root:
            return True

        if visited[node] is False:
            hascycle = explore(root,node,hascycle)
            if hascycle is True:
                return True
    return False


def acyclic():
    for i in range(n):
        if visited[i] is False:
            hascycle = explore(i,i,False)
            if hascycle is True:
                return 1
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    visited = [False for _ in range(n)]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic())
