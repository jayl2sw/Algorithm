from collections import deque


def dfs(start):
    visited.append(start)
    print(start, end=' ')
    for i in graph[start]:
        if i not in visited:
            dfs(i)


def bfs(start):
    visited_b =[start]
    q = deque()
    q.append(start)
    while q:
        x = q.popleft()
        print(x, end=' ')
        for i in graph[x]:
            if i not in visited_b:
                q.append(i)
                visited_b.append(i)


n, m, start = map(int,input().split())

graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()



visited = []


dfs(start)
print()
bfs(start)





