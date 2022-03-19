from collections import deque


def solution(m, n, puddles):
    graph = [[0] * m for _ in range(n)]
    for i in range(m):
        graph[0][i] = 1
        
    for puddle in puddles:
        graph[puddle[0] - 1][puddle[1] - 1] = 1e10

    q = deque()
    q.append((0, 0))

    graph[0][0] = 1

    while q:
        r, c = q.popleft()
        if r != 0 or c != 0:
            up = graph[r - 1][c] % 1000000007 if r - 1 >= 0 and graph[r - 1][c] != 1e10 else 0
            left = graph[r][c - 1] % 1000000007 if c - 1 >= 0 and graph[r][c - 1] != 1e10 else 0

            graph[r][c] = up + left

        if r + 1 < n and graph[r + 1][c] != 1e10:
            q.append((r + 1, c))
        if c + 1 < m and graph[r][c + 1] != 1e10:
            q.append((r, c + 1))

        print(graph)
        if graph[n - 1][m - 1] != 0:
            return graph[n - 1][m - 1] % 1000000007


print(solution(4,3,[[2,2]]))