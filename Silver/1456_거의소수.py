def check(n):
    return int(n ** 1/i) ** i == n






n, m = map(int, input().split())

d = [0] * m
for number in range(n, m):
    if check(number):
        d[number] = 1

print(d)

for idx in range(n, m):
    times = 2
    if idx ==1:
        d[idx] = 0
        continue
    while idx ** times < m:
        if d[idx] >= 1:
            d[idx ** times] = times
        times += 1

for i in range(n, m):
    if d[i] >= 2:
        print(i, end=' ')

total = 0
for i in d:
    if i >= 2:
        total += 1

print(d)
print(total)


