import sys
input = sys.stdin.readline
N, M = map(int, input().split())
board = [input() for _ in range(N)]
mins = []

for si in range(N-7):
    for sj in range(M-7):
        num1 = 0
        num2 = 0
        for a in range(si, si+8):
            for b in range(sj, sj+8):
                if (a+b) % 2 == 0:
                    if board[a][b] != 'W':
                        num1 += 1
                    else:
                        num2 += 1
                else:
                    if board[a][b] != 'B':
                        num1 += 1
                    else:
                        num2 += 1

        mins.append(num1)
        mins.append(num2)

print(min(mins))

