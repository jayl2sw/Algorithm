import sys
input = lambda: sys.stdin.readline().strip()

N = int(input())

primes = []
arr = [1] * (N+1)

for i in range(2, int(N ** (1/2)) + 1):
    if arr[i]:
        j = 2

        while i * j <= N:
            arr[i*j] = False
            j += 1

for num in range(2, N+1):
    if arr[num]:
        primes.append(num)

cnt = 0
tmp = 0
e = 0

for s in range(len(primes)):
    while tmp < N and e < len(primes):
        tmp += primes[e]
        e += 1

    if tmp == N:
        cnt += 1

    tmp -= primes[s]

print(cnt)
