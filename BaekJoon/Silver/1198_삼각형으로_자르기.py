from itertools import combinations
n = int(input())
array = []
for i in range(n):
    array.append(list(map(int,input().split())))

all_combi = list(combinations(array, 3))

mx = 0
for com in all_combi:
    x = []
    y = []
    for i in range(3):
        x.append(com[i][0])
        y.append(com[i][1])

    sq_width = max(x)-min(x)
    sq_height = max(y)-min(y)
    sq_area = sq_height * sq_width

    for i in range(3):
        for j in range(3):
            if i != j:
                sq_area = sq_area - (abs(x[i]-x[j]) * abs(y[i]-y[j]))/4

    if mx < sq_area:
        mx = sq_area

print(round(float(mx), 1))






