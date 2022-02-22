n = int(input())
array = []



a, b = map(int, input().split())
array.append(a)
array.append(b)
for i in range(1, n):
    a, b = map(int, input().split())
    array.append(b)

total = 0
while len(array) > 2:
    idx = array.index(max(array[1:-1]))
    total += array[idx-1] * array[idx] * array[idx+1]
    del array[idx]

print(total)