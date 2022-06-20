import sys

input = sys.stdin.readline
N = int(input().strip())

d = [0] * (N + 1)
d[1] = (0, 0)

for i in range(2, N+1):
    if not i % 3 and not i % 2:
        if d[i//2][0] > d[i//3][0]:
            d[i] = (d[i // 3][0] + 1, i // 3)
        else:
            d[i] = (d[i // 2][0] + 1, i // 2)
    elif not i % 3:
        if d[i-1][0] > d[i//3][0]:
            d[i] = (d[i//3][0] + 1, i//3)
        else:
            d[i] = (d[i - 1][0] + 1, i - 1)

    elif not i % 2:
        if d[i-1][0] > d[i//2][0]:
            d[i] = (d[i//2][0] + 1, i//2)
        else:
            d[i] = (d[i - 1][0] + 1, i - 1)

    else:
        d[i] = (d[i - 1][0] + 1, i - 1)

print(d[N][0])
while N > 0:
    print(N, end=" ")
    N = d[N][1]

print()





# N = int(input())
# INF = float('inf')
# d = [INF] * (N+1)
# b = [0]*(N+1)
# d[1] = 0
# b[1] = 0
#
#
# for i in range(2, N+1):
#     if not i % 3:
#         if d[i-1] < d[i//3]:
#             b[i] = i-1
#             d[i] = d[i-1] + 1
#         else:
#             b[i] = i//3
#             d[i] = d[i//3] + 1
#     elif not i % 2:
#         if d[i-1] < d[i//2]:
#             b[i] = i-1
#             d[i] = d[i - 1] + 1
#         else:
#             b[i] = i//2
#             d[i] = d[i // 2] + 1
#     else:
#         d[i] = d[i-1] + 1
#         b[i] = i-1
#
# print(d[N])
# while N > 0:
#     print(N, end=" ")
#     N = b[N]

