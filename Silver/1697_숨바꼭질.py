n, k = map(int,input().split())

d = [int(1e9)] * int(3 * 1e5)

d[n] = 0
for i in range(n):
    d[i] = abs(n-i)

d[n * 2] = 1
for i in range(n+1, k + 1000):
    if i % 2 == 0:
        d[i] = min(d[i-1] + 1, d[i + 1] + 1, d[i//2] + 1)
    else:
        d[i] = min(d[i-1] + 1 , d[i + 1] + 1)
    d[i * 2] = d[i] + 1

print(d[k])