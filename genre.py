path = [0] * 10
n = 5


def bbq(lev, sum):
    global path, n

    if sum > 7 : return
    if lev == n:
        for i in range(lev):
            print(path[i], end=' ')
        print(" = " + str(sum))
        return


    for i in range(6):
        path[lev] = i + 1
        bbq(lev +1, sum + i + 1)
        path[lev] = 0

bbq(0,0)