import heapq
import sys
input = sys.stdin.readline

def find(x):
    if head[x] == x:
        return x
    else:
        nxt = find(head[x])
        return nxt

V, E = map(int, input().split())
edges = []
for _ in range(E):
    s, e, cost = map(int, input().split())
    heapq.heappush(edges, (cost, s, e))

head = list(range(V+1))

cnt = 0
answer = 0
while edges:
    cost, s, e = heapq.heappop(edges)

    if find(s) == find(e):
        continue

    s, e = find(s), find(e)

    if s < e:
        head[e] = s
    else:
        head[s] = e


    cnt += 1
    answer += cost
    if cnt == V-1:
        break




print(answer)