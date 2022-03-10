def solution(triangle):
    for i in range(len(triangle)-1, 0, -1):
        for j in range(i):
            triangle[i-1][j] += max(triangle[i][j],triangle[i][j+1])
        print(triangle)
    return triangle[0][0]


triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))