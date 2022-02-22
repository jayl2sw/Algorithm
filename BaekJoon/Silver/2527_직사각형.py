def check(array):
    x1, y1, x2, y2, x3, y3, x4, y4 = array
    x = [x1, x2, x3, x4]
    y = [y1, y2, y3, y4]
    dx = [0] * 50001
    dy = [0] * 50001

    for i in range(x1, x2+1):
        dx[i] += 1
    for i in range(x3, x4+1):
        dx[i] += 1
    for j in range(x1, x2+1):
        dy[j] += 1
    for j in range(x3, x4+1):
        dy[j] += 1
    x_cover = dx.count(2)
    y_cover = dy.count(2)
    print(dx[81:91])
    print(dy[:601])

    if x_cover == 1 and y_cover == 1:
        return 'c'
    elif x_cover == 1 and y_cover >= 1 or x_cover >= 1 and y_cover == 1:
        return 'b'
    elif x_cover >= 1 and y_cover >= 1:
        return 'a'
    else:
        return 'd'

for i in range(4):
    array = list(map(int, input().split()))
    print(check(array))