import sys
from collections import deque
input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    N, K = map(int,input().split())
    costs = [-1]+list(map(int,input().split()))
    priority = [0] * (N + 1)
    graph = [[] for _ in range(N+1)]
    for _ in range(K):
        pre, post = map(int,input().split())
        priority[post] += 1
        graph[pre].append(post)

    W = int(input().strip())
    q = deque()

    for i in range(1, N+1):
        if priority[i] == 0:
            q.append(i)

    times = [0] * (N+1)
    while q:
        now = q.popleft()
        if now == W:
            print(times[now] + costs[now])
            break
        for nxt in graph[now]:
            priority[nxt] -= 1
            times[nxt] = max(times[nxt], times[now] + costs[now])
            if priority[nxt] == 0:
                q.append(nxt)



