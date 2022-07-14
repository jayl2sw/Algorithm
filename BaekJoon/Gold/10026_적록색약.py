from collections import deque
import sys

input = lambda:sys.stdin.readline().rstrip()

N = int(input())

arr = [input() for _ in range(N)]
visited = [[0] * N for _ in range(N)]


def bfs(si, sj):
    q = deque()
    q.append((si, sj))

    while q:
        ci, cj = q.popleft()
        visited[ci][cj] = 1
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == arr[ci][cj] and not visited[ni][nj]:
                q.append((ni, nj))

cnt1 = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)
            cnt1 += 1

for i in range(N):
    arr[i] = arr[i].replace('R','G')

cnt2 = 0
visited = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)
            cnt2 += 1

print(cnt1, cnt2)

