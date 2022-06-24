N = int(input())
K = int(input())

left = 1
right = N*N
ans = 0

while left <= right:
    mid = (left + right) // 2

    val = 0
    for i in range(1, N+1):
        val += min(N, mid//i)

    if val >= K:
        right = mid - 1
        ans = mid
    else:
        left = mid + 1
print(ans)


