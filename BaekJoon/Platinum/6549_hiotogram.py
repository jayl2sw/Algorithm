while True:
    arr = list(map(int,input().split()))
    N = len(arr)
    if N == 1 and arr[0] == 0:
        break
    result = 0
    for i in range(N):
        left = right = 0

        while i-left-1 >= 0 and arr[i - left - 1] >= arr[i]:
            left += 1
        while i + right + 2 <= N and arr[i + right + 1] >= arr[i]:
            right += 1

        if result < arr[i] * (left + right + 1):
            result = arr[i] * (left + right + 1)

    print(result)
