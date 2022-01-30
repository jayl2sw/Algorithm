n, k = map(int,input().split())

array = []

for i in range(n):
    array.append(int(input()))

array.sort(reverse=True)

count = 0
for coin in array:
    if k // coin >= 1:
        count += (k // coin)
        k %= coin

print(count)