from collections import deque

T = int(input())

for tc in range(1, T+1):
    F, N = map(int,input().split())
    arr = deque(list(map(int, input().split())))

    while True:
        _max = max(arr, key=lambda x: arr.count(x))
        flag = False
        if len(arr) == 1:
            break
        for _ in range(len(arr)):
            print(arr)
            if F < 2:
                break
            x = arr.popleft()
            if not flag and x == _max:
                flag = True
            else:
                arr.append(x)

            F -= 1

        if F < 2:
            break
        if len(arr) == 1:
            break

    print(f'#{tc} {arr[0]}')

