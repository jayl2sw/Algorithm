from itertools import combinations
from collections import deque
N, M, G, R = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]

def bfs(green, red):
    visited = [[0] * M for _ in range(N)]
    q = deque()
    cnt = 0
    for gi, gj in green:
        q.append((gi, gj, 'g'))
        visited[gi][gj] = -1
    for ri, rj in red:
        q.append((ri, rj, 'r'))
        visited[ri][rj] = -1

    while q:
        ci, cj, color = q.popleft()
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ni, nj = ci+di, cj+dj
            if 0<= ni<N and 0<= nj <M and (board[ni][nj] == 1 or board[ni][nj] == 2) and visited[ni][nj] != 'F' and visited[ni][nj] == 0 and visited[ni][nj]<999999:
                if visited[ci][cj] < 0:
                    visited[ni][nj] = visited[ci][cj] - 1
                    q.append((ni, nj, color))
                elif 0 <= visited[ni][nj] < 999999:

candidates = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 2:
            candidates.append((i, j))

for case in list(combinations(candidates, G+R)):
    greens = set(combinations(case, G))
    for green in greens:
        green = set(green)
        red = set(case)-green

        bfs(green, red)







