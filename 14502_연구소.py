# 14502 연구소
from itertools import combinations

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))


def breeding(x, y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    if graph[x][y] == 1:
        return False
    if graph[x+1][y] != 0 and graph[x-1][y] != 0 and graph[x][y-1] != 0 and graph[x][y+1] != 0:
        return False
    if graph[x][y] == 2:
        breeding(x + 1, y)
        breeding(x - 1, y)
        breeding(x, y + 1)
        breeding(x, y - 1)
        return False
    else:
        return False


def create_wall(x, y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return
    graph[x][y] = 1


space = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            space.append((i, j))
available_space = list(combinations(space, 3))

max = 0
for case in available_space:
    for x, y in case:
        space = 0
        create_wall(x, y)
        for i in range(n):
            for j in range(m):
                if graph[i][j] == 2:
                    breeding(i, j)
        for line in graph:
            for number in line:
                if number == 0:
                    space += 1
        if space >= max:
            max = space

print(space)
