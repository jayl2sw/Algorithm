import sys
from collections import deque

sys.stdin = open('input.txt')



def bfs():

    q = deque()
    q. append(1)
    count = 0

    while q:
        location = q.popleft()

        if location == 100:
            return count
        temp = list(range(location+1, location+7))
        for loc in range(location+1, location+7):
            if loc in ladders_start:
                temp.append(ladders_end[ladders_start.index(loc)])
                temp.remove(loc)
            if loc in snakes_start:
                temp.append(snakes_end[snakes_start.index(loc)])
                temp.remove(loc)
        for i in temp:
            q.append(i)




T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    ladders_start = []
    ladders_end = []
    for _ in range(n):
        a, b = map(int,input().split())
        ladders_start.append(a)
        ladders_end.append(b)
    snakes_start = []
    snakes_end =[]
    for _ in range(m):
        a, b = map(int,input().split())
        snakes_start.append(a)
        snakes_end.append(b)



    print(array)



