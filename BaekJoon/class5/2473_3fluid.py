import sys
input = sys.stdin.readline

N = int(input().strip())
arr = list(map(int, input().split()))

arr.sort()

left = 0
right = N-1
answer = []
temp = arr[left] + arr[right]
_min = int(1e9)
while left < right:
    for i in range(left+1, right):
        temp += arr[i]
        if _min > abs(temp):
            _min = abs(temp)
            answer = [arr[left], arr[i], arr[right]]
        temp -= arr[i]

    if temp < 0:
        temp -= arr[left]
        left += 1
        temp += arr[left]
    else:
        temp -= arr[right]
        right -= 1
        temp += arr[right]

print(" ".join(map(str, answer)))

