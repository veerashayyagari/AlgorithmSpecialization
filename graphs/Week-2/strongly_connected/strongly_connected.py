#Uses python3

import sys
import time

sys.setrecursionlimit(200000)

count = 1

def graphorder(vertex,graph,visited,post):
    global count
    visited[vertex] = True
    count += 1
    for node in graph[vertex]:
        if visited[node] is False:
            graphorder(node,graph,visited,post)
    post[vertex] = count
    count += 1

def dfs(graph):    
    post = [0 for _ in range(n)]
    visited = [False for _ in range(n)]
    for i in range(n):
        if visited[i] is False:
            graphorder(i,graph,visited,post)
    return post

def explore_scc(vertex,graph,scc,visited,post):
    visited[vertex] = True
    scc.add(post[vertex])
    
    for node in graph[vertex]:
        if visited[node] is False:
            explore_scc(node,graph,scc,visited,post)


def find_all_scc(graph,post):
    visited = [False for _ in range(n)]
    rem_nodes = sorted([(i,j) for i,j in enumerate(post)],key=lambda k:k[1],reverse=True)    
    result = 0

    while len(rem_nodes) != 0:
        scc = set()        
        max_index = rem_nodes[0][0]
        explore_scc(max_index,graph,scc,visited,post)
        result += 1
        rem_nodes = [t for t in rem_nodes if t[1] not in scc]       
    return result


def number_of_strongly_connected_components(actual_graph,reverse_graph):    

    #t0 = time.time()
    # Post Order for Reverse Graph
    graphpostorder = dfs(reverse_graph)
        

    # Find All SCC on actual graph based of post order
    components = find_all_scc(actual_graph,graphpostorder)    
    
    #t1 = time.time()

    #print(t1-t0)
    #print("Components :",components)
    return components

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    actual_graph = [[] for _ in range(n)]
    reverse_graph = [[] for _ in range(n)]
    for (a, b) in edges:
        actual_graph[a - 1].append(b - 1)
        reverse_graph[b-1].append(a-1)
    print(number_of_strongly_connected_components(actual_graph,reverse_graph))
