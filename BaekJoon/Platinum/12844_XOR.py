N = int(input())
arr = list(map(int, input().split()))
M = int(input())

result = 0
for a in arr:
    result ^= a
for _ in range(M):
    n, i, j, *k = map(int, input().split())
    if n == 2:
        print(result)
    elif n == 1:
        if j - i:
            result ^= k[0]
