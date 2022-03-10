def solution(N, number):
    d = [1e9] * 100
    d[N] = 1
    d[1] = 2

    k = N
    idx = 1
    while True:
        k = k * 10 + N
        idx += 1
        d[k] = idx
        if k > number:
            break

    for i in range(number+1):
        if i % N == 0:
            d[i] = min(d[i - N] + 1, d[i + N] + 1, d[i // N] + 1, d[i * N] + 1, d[i - 1] + 1, d[i + 1] + 1)
        else:
            d[i] = min(d[i - N] + 1, d[i + N] + 1, d[i * N] + 1, d[i-1]+2, d[i+1]+2)

    print(d[12])
    return d[number]


print(solution(5, 12))