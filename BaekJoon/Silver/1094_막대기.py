x = int(input())
result = []
while x >= 1:
    result.append(x % 2)
    x //= 2

print(sum(result))



