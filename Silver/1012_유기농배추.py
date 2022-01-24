graph = []


def bfs(x, y, m, n):
    if x < 0 or y < 0 or x >= m or y >= n:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        bfs(x + 1, y, m, n)
        bfs(x - 1, y, m, n)
        bfs(x, y + 1, m, n)
        bfs(x, y - 1, m, n)
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
    for i in range(m):
        for j in range(n):
            if bfs(i, j, m, n):
                count += 1
    print(count)
