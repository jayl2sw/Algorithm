n, m = map(int,input().split())

def check(n, m, x, y, i):
    nx = x+i
    ny = y+i
    a = graph[x][y]
    if nx >= n or ny >= m:
        return False
    else:
        if graph[nx][y] == a and a == graph[x][ny] and a == graph[nx][ny]:
            return True


graph = []

for i in range(n):
    graph.append(list(map(int, input())))


def find():
    k = min(m, n) - 1
    while True:
        if k == 0:
            return 1
        for i in range(n - k + 1):
            for j in range(m - k + 1):
                if check(n, m, i, j, k):
                    return k+1
        k -= 1


print(find()**2)

