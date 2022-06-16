import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
INF = float('inf')
graph = [[INF] * n for _ in range(n)]
for i in range(n):
    graph[i][i] = 0

for i in range(m):
    s, e, c = map(int,input().split())
    graph[s-1][e-1] = min(graph[s-1][e-1], c)

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

for i in range(n):
    for j in range(n):
        if graph[i][j] == INF:
            graph[i][j] = 0

for line in graph:
    print(" ".join(map(str, line)))