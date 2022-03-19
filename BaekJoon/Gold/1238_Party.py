import heapq

n, m, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
for i in range(m):
    start, end, time = map(int, input().split())
    graph[start].append((time, start, end))

q = []
for temp in graph[x]:
    heapq.heappush(q, temp)

d = [int(1e6)] * (n+1)
d[x] = 0
visited = [x]

while q:
    time, start, end = heapq.heappop(q)
    if d[end] > d[start] + time:
        d[end] = d[start] + time
    visited.append(end)
    for temp in graph[end]:
        if temp not in q and temp[2] not in visited:
            heapq.heappush(q, temp)


b = [int(1e6)] * (n+1)
b[x] = 0
visited_b = [x]


for temp in graph[x]:
    heapq.heappush(q, temp)
    
while q:
    time, start, end = heapq.heappop(q)
    if d[end] > d[start] + time:
        d[end] = d[start] + time
    visited.append(end)
    for temp in graph[end]:
        if temp not in q and temp[2] not in visited:
            heapq.heappush(q, temp)

