N, M = map(int,input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))

left = 1
right = 100000
answer = 0
while left <= right:
    mid = (right + left) // 2
    tmp = 0
    for i in arr:
        tmp += i // mid

    if tmp >= M:
        left = mid + 1
        answer = max(answer, mid)
    else:
        right = mid - 1

print(answer)