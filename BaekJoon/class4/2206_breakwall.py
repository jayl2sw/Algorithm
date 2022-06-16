import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int,input().split())
arr = [list(map(int, input().strip())) for _ in range(N)]
visited = [[[0]* 2 for _ in range(M)] for _ in range(N)]

print(arr)

q = deque()
q.append((0, 0, 1, 0))

while q:
    i, j, a, c = q.popleft()
    if i == N-1 and j == M-1:
        print(a)
        break
    for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < M:
            if c == 0:
                if not arr[ni][nj] and not visited[ni][nj][0]:
                    visited[ni][nj][0] = 1
                    visited[ni][nj][1] = 1
                    q.append((ni, nj, a+1, 0))
                elif arr[ni][nj]:
                    visited[ni][nj][1] = 1
                    q.append((ni, nj, a+1, 1))

            else:
                if not arr[ni][nj] and not visited[ni][nj][1]:
                    visited[ni][nj][1] = 1
                    q.append((ni, nj, a+1, 1))

else:
    print(-1)