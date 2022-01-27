import sys
input = sys.stdin.readline

n, m = map(int,input().split())

count = m - n + 1
d = [False] * count

i = 2
while i ** 2 < m:
    square = i ** 2
    remain = 0 if n % square == 0 else 1
    j = n // square + remain                    # 시작할 j

    while square * j <= m:
        if d[square * j - n] == False:
            d[square * j - n] = True
            count -=1
        j+=1

    i += 1

print(count)

# 에라토스테네스의 체


