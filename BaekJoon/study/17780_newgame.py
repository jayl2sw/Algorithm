import sys
from copy import deepcopy

input = sys.stdin.readline

def solution(idx):
    r, c, d = pieces[idx]
    if idx != check[r][c][0]:
        return 0

    nr, nc = r + dr[d], c + dc[d]

    if not 0 <= nr < N or not 0 <= nc < N or board[nr][nc] == 2:
        pieces[idx][2] = opp[d] # 방향 반대
        nr = r + dr[opp[d]]
        nc = c + dc[opp[d]]

        if not 0 <= nr < N or not 0 <= nc < N or board[nr][nc] == 2:
            return

    tmp = deepcopy(check[r][c])

    if board[nr][nc] == 1:
        tmp = tmp[::-1]

    # tmp 이동
    for piece in tmp:
        check[nr][nc].append(piece)
        pieces[piece][0] = nr
        pieces[piece][1] = nc

    # 이동 후 삭제
    check[r][c] = []

    # 종료 조건
    if len(check[nr][nc]) >= 4:
        return 1

    return


N, K = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
check = [[[] for _ in range(N)] for _ in range(N)]
pieces = []

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]
opp = [1, 0, 3, 2]

for i in range(K):
    row, column, direction = map(int, input().split())
    pieces.append([row-1, column-1, direction-1])
    check[row-1][column-1].append(i)

for time in range(1, 1001):
    for idx in range(K):
        if solution(idx):
            print(time)
            break
    else:
        continue
    break
else:
    print(-1)






