from collections import deque

def bfs(start):
    cnt = 1
    visited = [0 for _ in range(n+1)]
    visited[start] = 1
    queue = deque()
    queue.append(start)
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if not visited[v]:
                queue.append(v)
                visited[v] += 1
                cnt += 1
    return cnt

n, m = map(int,input().split())
graph = [[] for i in range(n+1)]

for i in range(m):
    a, b = map(int,input().split())
    graph[b].append(a)

result = []
max_cnt = 0
for i in range(1, n+1):
    cnt = bfs(i)
    if cnt > max_cnt:
        max_cnt = cnt
    result.append([i, cnt])

for i, cnt in result:
    if cnt == max_cnt:
        print(i, end=' ')
