N, C = map(int,input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))

arr.sort()

def solution(arr):
    left = 0
    right = arr[N-1]
    _max = right - left

    while right >= left:
        now = 0
        router = 0
        mid = (left + right) // 2
        for i in range(len(arr)):
            if arr[i] >= now:
                router += 1
                now = arr[i] + mid

        if router < C:
            right = mid -1
        else:
            _max = mid
            left = mid +1

    return _max

print(solution(arr))




