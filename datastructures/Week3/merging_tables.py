# python3

import sys


class Table:
    def __init__(self,id,rows):
        self._id = id
        self._rows = rows


def getParent(table):
    while table != parent[table]:
        parent[table] = getParent(parent[table])
        table = parent[table]

    return table

def merge(destination, source):
    global maxRows
    i_id = getParent(destination)
    j_id = getParent(source)

    if i_id == j_id:
        return

    if rank[i_id] > rank[j_id]:
        parent[j_id] = i_id
        tables[i_id]._rows += tables[j_id]._rows
        if maxRows < tables[i_id]._rows:
            maxRows = tables[i_id]._rows
    else:
        parent[i_id] = j_id
        tables[j_id]._rows += tables[i_id]._rows
        if maxRows < tables[j_id]._rows:
            maxRows = tables[j_id]._rows

        if rank[i_id] == rank[j_id]:
            rank[j_id] += 1


n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))
rank = [1] * n
parent = list(range(0, n))
tables = [Table(i,rowCount) for i,rowCount in enumerate(lines)]
maxRows = max(lines)
for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())    
    merge(destination - 1, source - 1)
    print(maxRows)
    
