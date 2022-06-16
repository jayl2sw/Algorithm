import sys

input = sys.stdin.readline

N, M = map(int, input().split())
array = [list(map(int,input().split())) for _ in range(N)]

for i in range(N):
    for j in range(1, N):
        array[i][j] += array[i][j-1]

for j in range(N):
    for i in range(1, N):
        array[i][j] += array[i-1][j]


for _ in range(M):
    x1, y1, x2, y2 = map(int,input().split())

    answer = array[x2 - 1][y2 - 1]
    if x1 - 2 > -1:
        answer -= array[x1 - 2][y2 - 1]
    if y1 - 2 > -1:
        answer -= array[x2 - 1][y1 - 2]
    if x1 - 2 > -1 and y1 - 2 > -1:
        answer += array[x1 - 2][y1 - 2]
    print(answer)



