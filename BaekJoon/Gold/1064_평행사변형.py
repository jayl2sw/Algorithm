x1, y1, x2, y2, x3, y3 = map(int, input().split())

if (x3 - x1)*(y1 - y2) == (y3 - y1)*(x1 - x2):
    print(-1.0)
else:
    p1 = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    p2 = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5
    p3 = ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5
    array = [p1, p2, p3]

    print(2*(max(array) - min(array)))