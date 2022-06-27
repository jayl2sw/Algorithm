# 미네랄 2
import sys
from collections import deque

def bfs(row, column):
    visited = [[0] * C for _ in range(R)]
    q = deque()
    q.append((row, column))
    result = []
    while q:
        row, column = q.popleft()
        if visited[row][column]:
            continue
        visited[row][column] = True
        result.append((row, column))

        for dr, dc in (1, 0), (-1, 0), (0, 1), (0, -1):
            nr, nc = row + dr, column + dc

            if 0 <= nr < R and 0 <= nc < C and arr[nr][nc] == 'x' and not visited[nr][nc]:
                q.append((nr, nc))

    return result


def solution(time, height):
    global now
    if not time % 2:
        for i in range(C):
            if arr[R - height - 1][i] == 'x':
                arr[R - height - 1][i] = '.'
                now -= 1
                if arr[R - height - 1][i+1] == 'x':
                    minerals = bfs(R - height - 1, i+1)
                else:
                    minerals = bfs(R - height - 2, i)
                if len(minerals) == now:
                    break
                else:
                    # 떨어지는 거 구현
                    depth = 1
                    flag = False
                    while True:
                        for mi, mj in minerals:
                            if not 0 <= mi+depth < R:
                                flag = True
                                break
                            if (mi+depth, mj) not in minerals and arr[mi+depth][mj] == 'x':
                                flag = True
                        if flag:
                            break
                        depth += 1



                    for mi, mj in minerals:
                        arr[mi][mj] = '.'
                        arr[mi+depth-1][mj] = 'x'
                    break


    else:
        for i in range(C-1, -1, -1):
            if arr[R - height - 1][i] == 'x':
                arr[R - height - 1][i-1]
                break


input = sys.stdin.readline
R, C = map(int,input().split())
arr = [list(input().strip()) for _ in range(R)]
now = 0

N = int(input())
for i in range(R):
    for j in range(C):
        if arr[i][j] == 'x':
            now += 1

heights = list(map(int, input().split()))
for i in range(len(heights)):
    solution(i, heights[i]-1)

for r in arr:
    print("".join(r))