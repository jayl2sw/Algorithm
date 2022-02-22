array = []
for _ in range(9):
    array.append(int(input()))

two = sum(array) - 100

for i in range(1<<9):
    count = 0
    total = []
    for j in range(9):
        if i & (1<<j):
            count += 1
            total.append(array[j])
        if count > 2:
            break
    if count == 2 and sum(total) == two:
        for dwarf in total:
            array.remove(dwarf)
        break

array.sort()
for i in array:
    print(i)
