opp = [1, 0]
N, M = map(int, input().split())
d = []
for _ in range(M):
    O, S, T = map(int, input().split())
    if not O:
        d.append(S)
        d.append(T+1)

    elif O:
        i = 0
        while d[i] < T:
            if d[i] > S:
                i += 1
            elif d[i] == S:
                if i % 2:
                    i


