def factorial(x):
    result = 1
    for i in  range(1, x+1):
        result *= i
    return result


def combination(n, m):
    if m < 0:
        return False
    elif m == 0:
        return 1
    son = factorial(n)
    mother = factorial(m) * factorial(n-m)
    return son / mother

n, m , k = map(int,input().split())

total = 0


for i in range(k):
    if m-i > n-m:
        continue
    up = combination(m, i) * combination(n - m, m - i)
    down = combination(n, m)
    total += up/down


print(1- total)