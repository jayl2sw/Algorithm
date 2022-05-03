x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

def CCW(x1, y1, x2, y2, x3, y3):
    if (y3 - y1) * (x2-x1) > (y2-y1) * (x3-x1):
        return -1
    elif (y3 - y1) * (x2-x1) == (y2-y1) * (x3-x1):
        return 0
    else:
        return 1


if CCW(x1, y1, x2, y2, x3, y3) * CCW(x1, y1, x2, y2, x4, y4) < 0 and CCW(x3, y3, x4, y4, x1, y1) * CCW(x3, y3, x4, y4, x2, y2) < 0:
    print(1)
else:
    print(0)
