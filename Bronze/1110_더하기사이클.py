n = int(input())
start = n
count = 0
while True:
    if n < 10:
        n = n * 11
        count += 1
    else:
        first = n // 10
        second = n % 10
        right = (first + second) % 10
        n = second * 10 + right
        count += 1

    if n == start:
        print(count)
        break