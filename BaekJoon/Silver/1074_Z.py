N, r, c = map(int, input().split())

ans = 0
while N != 0:
    N -= 1

    if r < 2 ** N and c < 2 ** N:
        ans += 4 ** N * 0

    elif r < 2 ** N < c:
        ans += 4 ** N * 1

    elif r > 2 ** N > c:
        ans += 4 ** N * 2

    else:
        ans += 4 ** N * 3

print(ans)

N, r, c = map(int, input().split())
ans = 0
while N != 0:
    N -= 1
    if r < 2 ** N and c < 2 ** N:
        ans += 4 ** N * 0
    elif r < 2 ** N < c:
        ans += 4 ** N * 1
    elif c < 2 ** N < r:
        ans += 4 ** N * 2
    else:
        ans += 4 ** N * 3

print(ans)
