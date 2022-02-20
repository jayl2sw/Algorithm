def dice(start, n, array):
    sum = 0
    max_d = []
    min_d = []
    for i in range(n):
        reverse_side = array[i][reference[array[i].index(start)]]
        max_d.append(max(start, reverse_side))
        min_d.append(min(start, reverse_side))
        start = reverse_side

    sum += max_d.count(6)
    sum += min_d.count(5)

    return sum

n = int(input())
reference = [5, 3, 4, 1, 2, 0]
array = [list(map(int,input().split())) for _ in range(n)]
min_v = int(1e9)
for i in range(1, 7):
    sub = dice(i, n, array)
    if min_v > sub:
        min_v = sub

print(n*6-min_v)


