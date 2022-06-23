N, M = map(int, input().split())
memories = list(map(int,input().split()))
cost = list(map(int,input().split()))
_max = sum(cost)
result = int(1e9)

# Knapsack과 똑같이 _max * n까지 만듬
dp = [[0] * _max for _ in range(N+1)]

for i in range(N):
    byte = memories[i]
    c = cost[i]

    for j in range(_max):
        if j < c:
            dp[i][j] = dp[i-1][j]
        else:
            # 같은 cost 내에서 현재 앱을 끈 뒤의 byte와 현재 앱을 끄지 않은 뒤의 byte를 비교
            dp[i][j] = max(byte + dp[i-1][j-c], dp[i-1][j])
        if dp[i][j] >= M:
            result = min(result, j)

if M != 0:
    print(result)
else:
    print(0)




