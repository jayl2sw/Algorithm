def isUnderPrime(n):
    count = 0
    if n == 1:
        return False
    i = 2
    while i <= n:
        if n % i == 0:
            count += 1
            n /= i

        else:
            i += 1
    return count


def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

#
# def solution(a, b):
#     count = 0
#     for i in range(a, b+1):
#         if isUnderPrime(i) == True:
#             count += 1
#
#     return count
#
#
# n, m = map(int,input().split())
#
# print(solution(n, m))

def solution(a, b):
    ran = b - a + 1
    d = [0] * ran
    count = 0
    for i in range(a, b+1):
        d[i-a] = isUnderPrime(i)

    for elem in d:
        if isPrime(elem):
            count += 1

    return count


print(solution(123, 456))