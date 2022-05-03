N, M = map(int, input().split())
def solution(i, arr):
    if i >= N+1:
        if len(arr) == M:
            print(' '.join(arr))
        return

    if len(arr) > M:
        return

    solution(i + 1, arr + [str(i)])
    solution(i + 1, arr)
    return

solution(1, [])