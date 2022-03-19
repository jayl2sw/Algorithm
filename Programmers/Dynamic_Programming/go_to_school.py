from collections import deque
from pprint import pprint

n = 5
m = 5
puddles = [[1,1]]
graph = [[0] * m for _ in range(n)]

for puddle in puddles:
    graph[puddle[0]-1][puddle[1]-1] = 1e9

q = deque()
q.append((0, 0))

graph[0][0] = 1

while q:
    r, c = q.popleft()
    if r != 0 or c != 0:
        up = graph[r - 1][c]%1000000007 if r - 1 >= 0 and graph[r-1][c] != 1e9 else 0
        left = graph[r][c - 1]%1000000007 if c - 1 >= 0 and graph[r][c-1] != 1e9 else 0

        graph[r][c] = up + left

    if r + 1 < n and graph[r + 1][c] != 1e9:
        q.append((r + 1, c))
    if c + 1 < m and graph[r][c + 1] != 1e9:
        q.append((r, c + 1))

    i
print(graph[n-1][m-1]%1000000007)