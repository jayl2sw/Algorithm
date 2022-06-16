# import sys
# input = sys.stdin.readline
#
# V, E = map(int, input().split())
# K = int(input())
# graph = [[] for _ in range(V+1)]
#
# for _ in range(E):
#     u, v, w = map(int,input().split())
#     graph[u].append((v, w))
#
# INF = float('inf')
# d = [INF] * (V+1)
# d[K] = 0
#
# visited = [False] * (V+1)
#
# while True:
#     nxt = -1
#     _min = INF
#     for i in range(1, len(d)):
#         if _min > d[i] and not visited[i]:
#             _min = d[i]
#             nxt = i
#
#     if nxt == -1:
#         break
#
#     visited[nxt] = True
#     for destination, cost in graph[nxt]:
#         d[destination] = min(d[destination], d[nxt] + cost)
#
# for i in range(1, len(d)):
#     if d[i] == INF:
#         print('INF')
#     else:
#         print(d[i])

import sys
import heapq

input = sys.stdin.readline

INF = float('inf')
V, E = map(int, input().split())
K = int(input())

dp = [INF] * (V+1)
heap = []
graph = [[] for _ in range(V+1)]

def dijkstra(start):
    dp[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        cost, now = heapq.heappop(heap)

        if dp[now] < cost:
            continue

        for w, nxt in graph[now]:
            nxt_w = w + cost

            if nxt_w < dp[nxt]:
                dp[nxt] = nxt_w
                heapq.heappush(heap, (nxt_w, nxt))

for _ in range(E):
    u, v, w = map(int,input().split())
    graph[u].append((w, v))

dijkstra(K)
for i in range(1, V+1):
    print("INF" if dp[i] == INF else dp[i])

