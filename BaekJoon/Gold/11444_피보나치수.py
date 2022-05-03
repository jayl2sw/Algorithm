def multi(m1, m2):
    temp = [[0]*2 for _ in range(2)]
    temp[0][0] = m1[0][0] * m2[0][0] + m1[0][1] * m2[1][0]
    temp[0][1] = m1[0][0] * m2[0][1] + m1[0][1] * m2[1][1]
    temp[1][0] = m1[1][0] * m2[0][0] + m1[1][1] * m2[1][0]
    temp[1][1] = m1[1][0] * m2[0][1] + m1[1][1] * m2[1][1]
    return temp

def ans(m1, start):
    temp = [[0] for _ in range(2)]
    temp[0] = m1[0][0] * start[0] + m1[0][1] * start[1]
    temp[1] = m1[1][0] * start[0] + m1[1][1] * start[1]
def power(matrix, n):
    if n == 1:
        return matrix
    elif n % 2:
        return multi(power(matrix, n-1), matrix)
    else:
        return multi(power(matrix, n//2), power(matrix, n//2))

matrix = [[1,1],[1,0]]
n = int(input())
if n < 3:
    print(1)
else:
    print(power(matrix, n)[0][1])

