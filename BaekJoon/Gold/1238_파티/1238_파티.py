import heapq

N, M, X = map(int, input().split())
graphCome = [[] for _ in range(N+1)]
graphBack = [[] for _ in range(N+1)]

for _ in range(M):
    start, end, time = map(int,input().split())
    graphCome[start].append((time, start, end))
    graphBack[end].append((time, end, start))

qCome = []
qBack = []
for temp in graphCome[X]:
    heapq.heappush(qCome, temp)

for temp in graphBack[X]:
    heapq.heappush(qBack, temp)

dCome = [int(1e6)] * (N+1)
dBack = [int(1e6)] * (N+1)
dCome[X] = 0
dBack[X] = 0

visitedCome = [X]
visitedBack = [X]

while qCome:
    time, start, end = heapq.heappop(qCome)
    if dCome[end] > dCome[start] + time:
        dCome[end] = dCome[start] + time
    visitedCome.append(end)
    for temp in graphCome[end]:
        if temp not in qCome and temp[2] not in visitedCome:
            heapq.heappush(qCome, temp)

while qBack:
    time, start, end = heapq.heappop(qBack)
    if dBack[end] > dBack[start] + time:
        dBack[end] = dBack[start] + time
    visitedBack.append(end)
    for temp in graphBack[end]:
        if temp not in qBack and temp[2] not in visitedBack:
            heapq.heappush(qBack, temp)

maxDistance = 0
print(dCome, dBack)
for i in range(1, len(dCome)):
    if maxDistance < dCome[i] + dBack[i]:
        maxDistance = dCome[i] + dBack[i]

print(maxDistance)