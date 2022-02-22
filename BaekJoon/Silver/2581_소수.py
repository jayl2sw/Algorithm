def check(number):
    if number == 1:
        return False
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True


n = int(input())
m = int(input())

result = []
for i in range(n, m+1):
    if check(i):
        result.append(i)

if not result:
    print(-1)
else:
    print(sum(result))
    print(result[0])