N, K = map(int,input().split())

items = []
for _ in range(N):
    W, V = map(int,input().split())
    bags.append((W, V))

dp = [[0] * (K+1) for _ in range(N+1)]

for i in bags:
    for j in range(1, K+1):
        dp[i][j] = max(dp[i-1][j], dp[i-1][j-bags[i-1][0]] + bags[i-1][1])

print(dp[-1][-1])
