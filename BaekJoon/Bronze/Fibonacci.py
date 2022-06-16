# 2747 피보나치수

n = int(input())

d = [0] * (n+1)
if n > 2:
    d[1] = 1
    d[2] = 1

    for i in range(2, n+1):
        d[i] = d[i-1] + d[i-2]

    print(d[n])

else:
    if n == 0:
        print(0)
    else:
        print(1)