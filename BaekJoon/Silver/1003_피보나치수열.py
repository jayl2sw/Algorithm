cases = int(input())

for i in range(cases):
    num = int(input())
    d = [[0,0]] * (num + 1)

    if num == 0:
        print(1, 0)
        continue
    d[0] = [1, 0]
    d[1] = [0, 1]

    for i in range(2,num+1):
        d[i] = [d[i-1][0] + d[i-2][0],d[i-1][1] + d[i-2][1]]

    print(d[num][0], d[num][1])
