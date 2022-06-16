# Backtracking
def check(x):
    for k in range(x):
        if row[x] == row[k] or abs(row[x] - row[k]) == x - k:
            return False
    return True
def solution(i):
    global answer
    if i == N:
        answer += 1

    else:
        for j in range(N):
            row[i] = j
            if check(i):
                solution(i+1)

N = int(input())
row = [0] * N
answer = 0
solution(0)
print(answer)