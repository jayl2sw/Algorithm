import sys
import heapq

sys.stdin = open('1150_input.txt')
input = sys.stdin.readline

n, k = map(int, input().split())

graph = []
for i in range(n):
    graph.append([chr(65+i), int(input())])

cables = []
for i in range(n-1):
    heapq.heappush(cables, (graph[i+1][1]-graph[i][1], chr(65+i), chr(66+i)))


sum = 0

for i in range(k):
    distance, start, end = heapq.heappop(cables)
    temp = 0
    cnt = 0
    for cable in cables:
        if cnt == 2:
            break
        if cable[2] == start:
            temp += cable[0]
            start = cable[1]
            cables.remove(cable)
            cnt += 1
        elif cable[1] == end:
            temp += cable[0]
            end = cable[2]
            cables.remove(cable)
            cnt += 1
    heapq.heappush(cables, (temp-distance, start, end))
    sum += distance


print(sum)


