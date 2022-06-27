import heapq
import sys

input = sys.stdin.readline

def dijkstra(standard, destination):
    visited = [False] * (N + 1)

    q = []
    heapq.heappush(q, (0, 1))

    while q:
        time, now = heapq.heappop(q)
        if now == destination:
            if time <= K: # 만약 destination 까지 오는데 standard 보다 큰 간선이 K개 내라면
                return True # 가능하다
            else: # 만약 K보다 많은
                return False

        if visited[now]:
            continue

        visited[now] = True

        for nxt, c in graph[now]:
            if not visited[nxt]:
                if c > standard:
                    heapq.heappush(q, (time + 1, nxt))
                else:
                    heapq.heappush(q, (time, nxt))
    return False


N, P, K = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(P):
    s, e, cost = map(int,input().split())
    graph[s].append((e, cost))
    graph[e].append((s, cost))

left = 0
right = 1000000
answer = -1

while left <= right:
    mid = (left + right) // 2
    if dijkstra(mid, N):  # answer는 해당 조건을 만족할 때 갱신
        right = mid - 1
        answer = mid
    else:
        left = mid + 1

print(answer)