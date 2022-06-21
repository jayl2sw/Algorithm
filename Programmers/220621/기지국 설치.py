import math

def solution(n, stations, w):
    answer = 0
    start = 0
    lens = []
    for station in stations:
        if station - w - 1 - start > 0:
            lens.append(station - w - 1 - start)
        start = station + w
    if n - start > 0:
        lens.append(n - start)

    for len in lens:
        answer += math.ceil(len/(w*2+1))

    return answer

print(solution(16, [9], 2))