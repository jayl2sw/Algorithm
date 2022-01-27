def turret(x1, y1, r1, x2, y2, r2):
    difference = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    if abs(r1 - r2) < difference < r1 + r2:
        return 2
    elif difference == 0 and r1 == r2:
        return -1
    elif r1 + r2 == difference or abs(r1 - r2) == difference:
        return 1
    else:
        return 0


n = int(input())
for i in range(n):
    a, b, c, d, e, f = map(int, input().split())
    print(turret(a, b, c, d, e, f))

