# # BackTracking
# def backtracking(n, idx, prob, visited):
#     global answer
#     if answer > prob:
#         return
#     if idx == n:
#         answer = prob
#         return
#
#     for j in range(n):
#         if not visited & 1 << j and array[idx][j]:
#             backtracking(n, idx+1, prob * array[idx][j], visited | 1 << j)
#
#
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     array = [list(map(lambda x: int(x)/100, input().split())) for _ in range(N)]
#
#     answer = 0
#
#     backtracking(N, 0, 1, 0)
#     answer*=100
#
#     print(f'#{tc} {answer:.6f}')

# DP
#
def solution(employee, tasks):
    if tasks == (1 << N) - 1:
        return 1

    if dp[tasks]:
        return dp[tasks]

    for i in range(N):
        if arr[employee][i] and not tasks & (1 << i):
            dp[tasks] = max(dp[tasks], arr[employee][i] * solution(employee+1, tasks | (1 << i)))

    return dp[tasks]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(lambda x:int(x)/100, input().split())) for _ in range(N)]

    dp = [0] * (1 << N)
    result = solution(0, 0) * 100
    print(result)
    print(dp)
