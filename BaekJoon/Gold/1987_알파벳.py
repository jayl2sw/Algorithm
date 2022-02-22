n, m = map(int,input().split())

array = []
for i in range(n):
    array.append(list(input()))

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

visited = [[-1] * m for i in range(n)]
print(visited)

def bfs(x, y):
    visited[x][y] = [array[x][y]]
    while True:
        count = 0
        for i in range(4):
            nx = x + dx[i]
            ny = x + dx[y]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                return False
            else:
                if array[nx][ny] not in visited[x][y]:
                    visited[nx][ny] = visited[x][y].append(array[nx][ny])

                    nx = x
                    ny = y
                count += 1
        if count == 4:
            break
bfs(0,0)
print(visited)
