N, K = map(int, input().split())

INF = float('inf')

d = [INF] * 101
idx = N
tmp = []

while idx <= 101:
    d[idx] = 0
    tmp.append(idx)
    idx *= 2

print(d)
