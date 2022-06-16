# 유니온 파인드 풀이
# 런타임 에러
from sys import setrecursionlimit

setrecursionlimit(10 ** 6)

def solution(k, room_number):
    answer = []
    parents = [0] * (k + 1)
    for i in range(k+1):
        parents[i] = i

    def find(target):
        if target == parents[target]:
            parents[target] += 1
            return target
        else:
            parents[target] = find(parents[target + 1])
            return parents[target]

    for i in range(len(room_number)):
        rn = find(room_number[i])
        print(i, rn, parents)
        answer.append(rn)
    return answer

k = int(1e12)
room_number = [1] * 3

print(solution(k, room_number))