#  Longest Bitonic Subsequence

N = int(input())
arr = list(map(int, input().split()))
r_arr = arr[::-1]
di = [1] * N
dd = [0] * N

for i in range(1, N):
    for j in range(i):
        if arr[i] > arr[j]:
            di[i] = max(di[i], di[j] + 1)
        if r_arr[i] > r_arr[j]:
            dd[i] = max(dd[i], dd[j] + 1)

_max = 0
for i in range(N):
    if _max < di[i] + dd[N - 1 - i]:
        _max = di[i] + dd[N - 1 - i]

print(_max)


