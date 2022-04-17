N, Q = map(int,input().split())
arr = list(map(int,input().split()))
for _ in range(Q):
    x, y, a, b = map(int,input().split())
    print(sum(arr[x-1:y]))
    arr[a-1] = b