def check(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True

n = int(input())
array = list(map(int, input().split()))

count = 0

for i in array:
    if check(i):
        count +=1

print(count)