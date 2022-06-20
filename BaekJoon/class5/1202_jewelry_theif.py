import heapq
import sys

input = sys.stdin.readline

N, K = map(int,input().split())
gems = []
for _ in range(N):
    weight, value = map(int, input().split())
    heapq.heappush(gems, (weight, value))

bags = []
for _ in range(K):
    capacity = int(input().strip())
    heapq.heappush(bags, capacity)

answer = 0
available = []

for _ in range(K):
    capacity = heapq.heappop(bags)

    while gems and capacity >= gems[0][0]:
        weight, value = heapq.heappop(gems)
        heapq.heappush(available, -value)

    if available:
        answer -= heapq.heappop(available)

print(answer)