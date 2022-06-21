from collections import defaultdict
def solution(land, P, Q):
    N = len(land)
    N2 = N**2
    d = defaultdict(int)
    total = 0
    for i in range(N):
        for j in range(N):
            total += land[i][j]
            d[land[i][j]] += 1

    heights = []
    for i in d.keys():
        heights.append(i)

    heights.sort(reverse=True)






    return _min


print(solution([[4, 4, 3], [3, 2, 2], [ 2, 1, 0 ]], 5, 3))
