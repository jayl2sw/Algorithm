def check(aa, bb):
    idx = 2
    while True:
        temp = aa - bb
        if temp < 0:
            break
        aa = bb
        bb = temp
        idx += 1
    return idx



def continuing_number(x):
    max_v = 3
    max_n = 0
    for number in range(n//2, n):
        temp = check(x, number)
        if temp > max_v:
            max_n = number
            max_v = temp

    print(max_v)
    return max_n

def pnt(a, b):
    while True:
        print(a, end=' ')
        t = a - b
        if t < 0:
            print(b, end='')
            break
        a = b
        b = t

n = int(input())
result = continuing_number(n)
pnt(n, result)
