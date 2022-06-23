#  Longest Increasing Subsequence
from bisect import bisect_left

N = int(input())
data = list(map(int, input().split()))

# record = 모든 수의 최장 수열의 길이를 저장하는 배열
record = [0] * N
# dp = 해당 dp에 임시로 저장하는 배열(최대 길이를 알기 위해)
dp = [data[0]]
record[0] = 1


for i in range(1, N):
    # 기존 최대값보다 큰 값이 들어오면 dp에 추가하고 record에 기록
    if dp[-1] < data[i]:
        dp.append(data[i])
        record[i] = len(dp)

    # 만약 기존 최대값보다 작은 값이 들어오면 dp에서 현재 값보다 작은 값을 찾는다.
    # bisect_left를 사용하여 현재 들어갈 index를 찾음 => 현재값보다 작은 것 갯수 찾음
    else:
        idx = bisect_left(dp, data[i])
        dp[idx] = data[i]
        record[i] = idx + 1

ans = []
find_dp = len(dp)

# 최대 dp를 가지는 수부터 역으로 하나씩 담는다.
for i in range(len(record) -1, -1, -1):
    if record[i] == find_dp:
        ans.append(data[i])
        find_dp -= 1
    if find_dp < 1:
        break

print(len(ans))
print(*ans[::-1])
