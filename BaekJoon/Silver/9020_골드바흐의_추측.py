array = [False] * 10001


def isPrime(n):
    if n == 1:
        return
    for i in range(2, n // 2 + 1):
        if not n % i:
            return
    array[n] = True
    return


for i in range(2, 10001):
    isPrime(i)

T = int(input())
for tc in range(T):
    k = int(input())
    a = k // 2
    b = k // 2
    while True:
        if array[a] and array[b]:
            break
        a -= 1
        b += 1
    print(a, b)
