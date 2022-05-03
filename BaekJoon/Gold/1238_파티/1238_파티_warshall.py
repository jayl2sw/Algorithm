INF = int(1e7)
N, M, X = map(int,input().split())
warshall = [[INF] * (N+1) for _ in range(N+1)]

for i in range(N+1):
    warshall[i][i] = 0

for _ in range(M):
    start, end, distance = map(int, input().split())
    warshall[start][end] = distance

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            warshall[i][j] = min(warshall[i][j], warshall[i][k]+warshall[k][j])

max_value = 0
for i in range(1, N+1):
    max_value = max(max_value, warshall[i][X] + warshall[X][i])

print(max_value)