import sys
input = sys.stdin.readline

N = int(input().strip())
arr = [list(map(int,input().split())) for _ in range(N)]

INF = float('inf')
d = [[INF] * N for _ in range(N)]
for i in range(N):
    d[i][i] = 0

for i in range(1, N):
    for j in range(0, N-i):
        if i == 1:
            d[j][j+1] = arr[j][0] * arr[j][i] * arr[j+1][1]
        else:
            for k in range(j, j+i):
                d[j][j+i] = min(d[j][j+i],
                                d[j][k] + d[k+1][j+i] + arr[j][0] * arr[k][1] * arr[j+i][1])

print(d[0][N-1])
