def game(x, y):
    if x == 0:
        return -1
    if x <= y:
        return -1
    defeats = x - y
    z =  (y * 100) // x # 퍼센테이지
    if z == 99:
        return -1
    if defeats * 100 / (100 - z - 1) - int(defeats * 100 / (100 - z - 1)) == 0:
        remain = 0
    else:
        remain = 1
    total = int(defeats * 100 / (100 - z - 1)) + remain

    return total - x


x, y = map(int,input().split())

print(game(x, y))