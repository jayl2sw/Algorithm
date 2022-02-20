import sys

n = int(sys.stdin.readline())

if n % 2 == 0 or n % 5 == 0:
    print(-1)
else:
    result = 1
    ans = 1
    while result % n :
        result = (result % n) * 10 + 1
        ans += 1
    print(ans)


