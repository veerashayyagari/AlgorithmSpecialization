#Uses python3

import sys

def lcs3(a, b, c):
    m = len(a) + 1
    n = len(b) + 1
    l = len(c) + 1
    matrix = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(l)]

    for i in range(1,m):
        for j in range(1,n):
            for k in range(1,l):
                insertion = matrix[k-1][j-1][i]
                deletion = matrix[k][j][i-1]
                insertion_j = matrix[k-1][j][i-1]
                deletion_j = matrix[k][j-1][i]
                insertion_k = matrix[k][j-1][i-1]
                deletion_k = matrix[k-1][j][i]
                mismatch = matrix[k-1][j-1][i-1]
                match = matrix[k-1][j-1][i-1] + 1

                if a[i-1] == b[j-1] and b[j-1] == c[k-1]:
                    matrix[k][j][i] = max(insertion,deletion,insertion_j,deletion_j,insertion_k,deletion_k,match)
                else:
                    matrix[k][j][i] = max(insertion,deletion,insertion_j,deletion_j,insertion_k,deletion_k,mismatch)
    return matrix[l-1][n-1][m-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
