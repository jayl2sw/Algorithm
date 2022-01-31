n = int(input())


if n % 2 == 0 or n % 5 == 0:
    print(-1)

result = 1

while True:
    if int(result) % n == 0:
        print(len(str(result)))
        break
    else:
        result = result * 10 + 1



