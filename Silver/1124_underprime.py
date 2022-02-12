def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def factorization(x):
    d = 2
    count = 0
    while d <= x:
        if x % d == 0:
            count += 1
            x = int(x / d)
        else:
            d += 1
    return count


a, b = map(int, input().split())

count = 0

for i in range(a, b + 1):
    if isPrime(factorization(i))==True:
        count += 1


print(count)

