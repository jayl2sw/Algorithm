N = int(input())
arr = list(map(int,input().split()))

dp = []
for i in range(N):
    dp.append((1, i))

_max = 0
idx = -1
for i in range(1, N):
    for j in range(i):
        if arr[i] > arr[j]:
            if dp[i][0] < dp[j][0] + 1:
                dp[i] = (dp[j][0] + 1, j)
                if dp[i][0] > _max:
                    _max = dp[i][0]
                    idx = i

print(_max)
answer = []
answer.append(arr[idx])
while idx > 0:
    idx = dp[idx][1]
    answer.append(arr[idx])

print(" ".join(map(str, answer[::-1])))

