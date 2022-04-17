import heapq

N = int(input())
q = []
for _ in range(N):
    A, B, *C = map(int, input().split())
    if A == 1:
        print(q.pop(1))
    else:
        C = C[0]
        if C > 0:
            for _ in range(C):
                heapq.heappush(q, B)
        else:
            q.remove(B)
