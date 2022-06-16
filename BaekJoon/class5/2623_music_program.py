from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
priority = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    arr = list(map(int,input().split()))
    for i in range(1, len(arr) - 1):
        graph[arr[i]].append(arr[i+1])
        priority[arr[i+1]] += 1



def topology_sort():
    q = deque()
    result = []

    for i in range(1, N+1):
        if priority[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            priority[i] -= 1

            if priority[i] == 0:
                q.append(i)

    if len(result) != N:
        print(0)
    else:
        for num in result:
            print(num)

topology_sort()
