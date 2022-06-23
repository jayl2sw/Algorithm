N = int(input())

table = [list(map(int,input().split())) for _ in range(N)]
table2 = [table[i][:] for i in range(N)]

for i in range(1, N):
    table[i][0] += max(table[i-1][0], table[i-1][1])
    table2[i][0] += min(table2[i-1][0], table2[i-1][1])
    for j in range(1,N-1):
        table[i][j] += max(table[i-1][j-1], table[i-1][j], table[i-1][j+1])
        table2[i][j] += min(table2[i - 1][j - 1], table2[i - 1][j], table2[i - 1][j + 1])

    table[i][N-1] += max(table[i - 1][N-2], table[i - 1][N-1])
    table2[i][N - 1] += min(table2[i - 1][N - 2], table2[i - 1][N - 1])

print(max(table[-1]), min(table2[-1]))