import sys



N, Q = map(int, sys.stdin.readline().split())
arr = [0] * (N + 1)
for _ in range(Q):
    t, p, q = map(int, input().split())
    if t == 1:
        arr[p] = q
    else:
        print(sum(arr[p:q+1]))






