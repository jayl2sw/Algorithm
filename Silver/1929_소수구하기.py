def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def prime(a, b):
    for number in range(a, b+1):
        if isPrime(number):
            print(number)


n, m = map(int,input().split())
prime(n,m)