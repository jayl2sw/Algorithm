# def solution(n, lost, reserve):
#
#     reserve = set(reserve)
#
#     for size in [0, 1, -2]:
#         lost = set(map(lambda x : x+size, lost))
#         reserve, lost = reserve - lost, lost - reserve
#
#     return n - len(lost)
#
#

def solution(n, lost, reserve):
    _reverse = set(r for r in reserve if r not in lost)
    _lost = set(l for l in lost if l not in reserve)
    for r in _reverse:
        if r-1 in _lost:
            _lost.remove(r-1)
        elif r+1 in _lost:
            _lost.remove(r+1)
    return n - len(_lost)

print(solution(5, [2, 4], [1, 3, 5]))