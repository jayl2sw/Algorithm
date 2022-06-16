import heapq
V = int(input())
q =[]
for _ in range(V):
    s, *args = map(int,input().split())
    for i in range(len(args)//2):
        if args[2*i] == -1:
            break
        heapq.heappush(q, (-args[2*i+1], args[2*i], s))

visited = [V]
while q:
    cost, s, e = heapq.heappop()
