import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()

N, M = map(int,input().split())
switch = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    i1, j1, i2, j2 = map(int,input().split())
    switch[i1-1][j1-1].append((i2-1, j2-1))

answer = 1
visited = [[False] * N for _ in range(N)]
visited[0][0] = 1
lights = [[0] * N for _ in range(N)]
lights[0][0] = 1
q = deque()
q.append((0,0))
while q:
    i, j = q.popleft()
    visited[i][j] = 1
    for si, sj in switch[i][j]:
        if not lights[si][sj]:
            lights[si][sj] = 1
            answer += 1
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                ni, nj = si+di, sj+dj
                if 0 <= ni < N and 0 <= nj < N and visited[ni][nj]:
                    q.append((si, sj))

    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and lights[ni][nj]:
            q.append((ni, nj))

print(answer)

