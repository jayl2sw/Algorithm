import sys
input = sys.stdin.readline
N, K = map(int,input().split())

d = [[0] * (K+1) for _ in range(N)]

for i in range(N):
    W, V = map(int, input().split())
    if i == 0:
        for j in range(W, K+1):
            d[i][j] = V
    else:
        for j in range(0, K+1):
            if j >= W:
                d[i][j] = max(d[i-1][j], d[i-1][j-W] + V)
            else:
                d[i][j] = d[i - 1][j]

print(d[-1][-1])
