from collections import deque
import sys

input = sys.stdin.readline
N, M = map(int,input().split())

priority = [0] * (N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    priority[e] += 1

q = deque()
for i in range(1, len(priority)):
    if priority[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    print(now, end=" ")
    for nxt in graph[now]:
        priority[nxt] -= 1
        if priority[nxt] == 0:
            q.append(nxt)




