import sys
import heapq
input = sys.stdin.readline

N, K = map(int,input().split())
jewelries = []
for _ in range(N):
    m, v = map(int, input().split())
    heapq.heappush(jewelries, (-m, v))

bags = []
for _ in range(K):
    heapq.heappush(bags, -int(input().strip()))

answer = 0
while bags:
    bag = -heapq.heappop(bags)

    while jewelries:
        m, v = heapq.heappop(jewelries)
        if bag > -m:
            print(answer)
            answer += v
            break

print(answer)

