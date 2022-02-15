# input 불러오기
import sys
sys.stdin = open('input.txt')
# 총 10번 반복
for i in range(10):
    # tc 입력
    tc = input()
    # 사다리 경로 100x100 행렬 입력
    arr = [list(map(int, input().split())) for _ in range(100)]
    start = []
    for j in range(100):
        if arr[0][j] == 1:
            start.append(j)
    # 각각 좌 우 하 방향
    # dx = [0, 0, 1]
    # dy = [-1, 1, 0]
    for s in start:
        now_x = 0
        now_y = s

        while now_x < 99:
            # 좌측 탐측
            if now_y > 0 and arr[now_x][now_y-1] == 1:
                arr[now_x][now_y] = 3
                now_y -= 1
            elif now_y < 99 and arr[now_x][now_y+1] == 1:
                arr[now_x][now_y] = 3
                now_y += 1
            elif arr[now_x + 1][now_y] == 1:
                arr[now_x][now_y] = 3
                now_x += 1

        for x in range(100):
            for y in range(100):
                if arr[x][y] == 3:
                    arr[x][y] = 1

        if arr[now_x][now_y] == 2:
            print(f'#{tc} {s}')
            break