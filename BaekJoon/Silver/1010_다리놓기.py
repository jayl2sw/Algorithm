def factorial(n):
    num = 1
    for i in range(1, n+1):
        num *= i
    return num

n = int(input())
ans = []
for i in range(n):
    n, m = map(int, input().split())
    if n ==0 or m == 0:
        print(0)
    else:
        print((int(factorial(m) // factorial(n) / factorial(m-n))))


