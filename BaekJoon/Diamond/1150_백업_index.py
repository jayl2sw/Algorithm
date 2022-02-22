import sys
import heapq


def change(tuple):
    a, b = tuple
    return (b, a)


def delete_push(idx):
    print((change(idxs[idx[0]-1])))


sys.stdin = open('1150_input.txt')
input = sys.stdin.readline

n, k = map(int, input().split())

graph = []
for i in range(n):
    graph.append(int(input()))

idxs = []
cables = []
for i in range(n-1):
    heapq.heappush(cables, (graph[i+1]-graph[i], (i, i+1)))
    heapq.heappush(idxs, ((i, i+1), graph[i+1]-graph[i]))

total = 0
for i in range(k):
    distance, idx = heapq.heappop(cables)
    total += distance
    temp = 0
    print(delete_push(idx))








print(sum)
