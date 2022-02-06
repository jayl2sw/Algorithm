from collections import deque

n, k = map(int, input().split())

MAX = 10 ** 5
dist = [0] * (MAX + 1)

def bfs():
    q = deque()
    q.append(n)

    while q:
        x = q.popleft()
        if x == k:
            print(dist[x])
            return

        for i in (x + 1, x - 1, x * 2):
            if 0 <= i <= MAX and dist[i] == 0:
                dist[i] = dist[x] + 1
                q.append(i)



bfs()