n = input()
d = [0] * 10

for i in n:
    if i == '6' or i == '9':
        if d[6] > d[9]:
            d[9] += 1
        else:
            d[6] += 1
    else:
        d[int(i)] += 1

print(max(d))

