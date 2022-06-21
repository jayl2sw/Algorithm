def solution(sticker):
    N = len(sticker)
    if N == 1:
        return sticker[0]

    d = [0] * N

    d[0] = sticker[0]
    d[1] = max(sticker[0], sticker[1])
    for i in range(2, N):
        d[i] = max(d[i - 1], d[i - 2] + sticker[i])

    a1 = d[N - 2]

    d[0] = 0
    d[1] = sticker[1]
    for i in range(2, N):
        d[i] = max(d[i - 1], d[i - 2] + sticker[i])

    a2 = d[N - 1]

    answer = max(a1, a2)

    return answer


print(solution([14, 6, 5, 11, 3, 9, 2, 10]))
