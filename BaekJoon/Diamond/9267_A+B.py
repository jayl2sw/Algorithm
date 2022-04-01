a, b, S = map(int, input().split())

d = [0] * (max(a, b) * S +1)

d[3] = 1
d[4] = 1

# for i in range(S):
#     d[i] = 1 if d[i-a] ==1 or d[i-b] == 1 or
