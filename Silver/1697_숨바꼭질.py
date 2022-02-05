# n, k = map(int,input().split())
#
# d = [int(1e9)] * int(2 * 1e5 + 2)
#
# d[n] = 0
# for i in range(n):
#     d[i] = n-i
#     d[i*2] = d[i]+1
#
# d[n * 2] = 1
# for i in range(n+1, k+1):
#     if i % 2:
#         d[i] = min(d[i-1], d[i+1]) +1
#     else:
#         d[i] = min(d[i-1], d[i+1],d[i+2] + 1) + 1
#     d[i*2] = d[i] + 1
#
#
#
# print(d[k])

from collections import deque


def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(dist[x])
            break
        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx <= MAX and not dist[nx]:
                dist[nx] = dist[x] + 1
                q.append(nx)


MAX = 10 ** 5
dist = [0] * (MAX + 1)
n, k = map(int, input().split())
bfs()
