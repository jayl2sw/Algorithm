graph = []


def bfs(x, y, n, m):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        bfs(x + 1, y, n, m)
        bfs(x - 1, y, n, m)
        bfs(x, y + 1, n, m)
        bfs(x, y - 1, n, m)
        return True
    else:
        return False


cases = int(input())

for case in range(cases):
    m, n, k = map(int, input().split())

    graph = [[0] * m for _ in range(n)]


    for _ in range(k):
        y, x = map(int, input().split())
        graph[x][y] = 1


    count = 0
    for i in range(n):
        for j in range(m):
            if bfs(i, j, n, m):
                count += 1
    print(count)
