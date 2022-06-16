import sys
import heapq
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    q = []
    rq = []
    n = int(sys.stdin.readline())
    for i in range(n):
        _input = sys.stdin.readline()

        if _input[0] == 'I':
            heapq.heappush(q, int(_input.split()[1]))
            heapq.heappush(rq, -int(_input.split()[1]))

        else:
            if len(q) != 0:
                if int(_input.split()[1]) == 1:
                    heapq.heappop(rq)
                else:
                    heapq.heappop(q)
            else:
                continue

    print(q)
    print(rq)