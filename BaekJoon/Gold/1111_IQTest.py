N = int(input())
arr = list(map(int, input().split()))

result = 'B'
if len(arr) == 1:
    result = 'A'

elif len(arr) == 2:
    if arr[0] == arr[1]:
        result = arr[0]
    else:
        result = 'A'

elif len(arr) > 2:
    if arr[1] - arr[0] != 0:
        a = int((arr[2] - arr[1]) / (arr[1] - arr[0]))
        b = int(arr[1] - arr[0] * a)
    elif arr[2] - arr[1] == 0:
        a, b = 1, 0
    else:
        a = 0
        b = int(1e9)

    for i in range(3, len(arr)):
        if a * arr[i-1] + b == arr[i]:
            continue
        else:
            break
    else:
        result = int(a * arr[-1] + b)

print(result)


