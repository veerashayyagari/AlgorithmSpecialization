# Uses python3

def Apply_Operator(d1,d2,op):
    if op == '+':
        return d1+d2
    elif op == '-':
        return d1-d2
    else:
        return d1*d2   

def MinMax(i,j,M,m,ops):
    maximum = float('-inf')
    minimum = float('inf')
    for k in range(i,j):
        a = Apply_Operator(M[i][k],M[k+1][j],ops[k])
        b = Apply_Operator(M[i][k],m[k+1][j],ops[k])
        c = Apply_Operator(m[i][k],M[k+1][j],ops[k])
        d = Apply_Operator(m[i][k],m[k+1][j],ops[k])
        minimum = min(a,b,c,d,minimum)
        maximum = max(a,b,c,d,maximum)
    return (minimum,maximum)

def get_maximum_value(dataset):
    data = list(dataset)
    n = len(data)
    digits = list(map(int,data[0:n:2]))
    ops = data[1:n:2]
    matrix_length = len(digits)
    M = [[0 for _ in range(matrix_length)] for _ in range(matrix_length)]
    m = [[0 for _ in range(matrix_length)] for _ in range(matrix_length)]
    for k in range(matrix_length):
        M[k][k] = digits[k]
        m[k][k] = digits[k]

    j = 1

    while j < matrix_length:
        i = 0
        while i+j < matrix_length:
            minimum,maximum = MinMax(i,i+j,M,m,ops)
            M[i][i+j] = maximum
            m[i][i+j] = minimum
            i += 1
        j += 1

    return M[0][matrix_length-1]





if __name__ == "__main__":
    print(get_maximum_value(input()))
