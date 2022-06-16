import sys
input = sys.stdin.readline

p = 1000000007

def multi(a, b):
    temp = [[0] * len(b[0]) for _ in range(2)]
    for i in range(2):
        for j in range(len(b[0])):
            t = 0
            for k in range(2):
                t += a[i][k]*b[k][j]
            temp[i][j] = t % p
    return temp

def power(mat, n):
    if n == 1:
        return mat
    elif n % 2:
        return multi(power(mat, n-1), mat)
    else:
        return power(multi(mat, mat), n//2)

mat = [[1, 1], [1, 0]]
start = [[1], [1]]
n = int(input())

if n < 3:
    print(1)
else:
    print(multi(power(mat, n-2), start)[0][0])


