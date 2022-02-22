n = int(input())
arr = list(map(int,input().split()))

count = 1
max_count = 1
for i in range(1, len(arr)):
    if arr[i-1] <= arr[i]:
        count += 1
        if max_count < count:
            max_count = count
    else:
        count = 1

count = 1
for i in range(1, len(arr)):
    if arr[i-1] >= arr[i]:
        count += 1
        if max_count < count:
            max_count = count
    else:
        count = 1

print(max_count)