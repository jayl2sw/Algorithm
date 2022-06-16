N = int(input())
arr = list(map(int,input().split()))
arr.sort()

left = 0
right = N - 1
_min = int(2e9)
answer = (arr[0], arr[N-1])
while left < right:
    print(left, right)
    if abs(arr[left] + arr[right]) < _min:
        _min = abs(arr[left] + arr[right])
        answer = (arr[left], arr[right])

    print(abs(arr[left]),abs(arr[right]), abs(arr[left]) < abs(arr[right]))
    if abs(arr[left]) < abs(arr[right]):
        right -= 1
    else:
        left += 1

print(" ".join(map(str, answer)))