n = int(input())
numbers = list(map(int,input().split()))

count = 0
for number in numbers:
    array = []
    for i in range(2, number+1):
        if number % i == 0:
            array.append(i)
    if len(array) == 1:
         count += 1

print(count)