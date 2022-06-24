#  Longest Increasing Subsequence
from bisect import bisect_left

N = int(input())
data = list(map(int, input().split()))

# 모든 수의 최장 수열의 길이를 저장하는 배열
record = [0] * N
# dp: 해당 dp에 임시로 저장하는 배열(최대 길이를 알기 위해)
dp = [data[0]]
record[0] = 1


for i in range(1, N):
    if dp[-1] < data[i]:
        dp.append(data[i])
        record[i] = len(dp)
    else:
        idx = bisect_left(dp, data[i])
        dp[idx] = data[i]
        record[i] = idx + 1

ans = []
find_dp = len(dp)
for i in range(len(record) -1, -1, -1):
    if record[i] == find_dp:
        ans.append(data[i])
        find_dp -= 1
    if find_dp < 1:
        break

print(len(ans))
print(*ans[::-1])
