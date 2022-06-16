N = input()
n = int(N)

start = max(n - len(N) * 10, 0)
for number in range(start, n):
    tmp = number
    for i in str(number):
        tmp += int(i)
    if tmp == n:
        print(number)
        break
else:
    print(0)