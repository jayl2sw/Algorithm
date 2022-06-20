# import sys
#
# input = sys.stdin.readline
#
# def solution(now, visited):
#     if visited == (1 << N) - 1:
#         return 0
#
#     # if dp[visited] != int(2e7):
#     #     return dp[visited]
#
#     for i in range(N):
#         if i != now and not (1 << i) & visited:
#             dp[visited] = min(dp[visited], graph[now][i] + solution(now+1, visited|(1<<i)))
#
#     return dp[visited]
#
#
#
# N = int(input().strip())
# dp = [int(2e7)] * (1 << N)
# graph = [list(map(int,input().split())) for _ in range(N)]
# print(solution(0,1))
# print(dp)

import sys

input = sys.stdin.readline

def solution(i, visited, temp, last):
    global _min

    if _min < temp:
        return

    if i == N-1:
        if _min > temp + graph[last][0]:
            _min = temp + graph[last][0]

    for j in range(N):
        if j != i and j != 0 and not (1 << j) & visited:
            solution(i+1, visited | (1 << j), temp + graph[i][j], j)


N = int(input())
_min = float('inf')
graph = [list(map(int,input().split())) for _ in range(N)]

solution(0,0,0,-1)

print(_min)
