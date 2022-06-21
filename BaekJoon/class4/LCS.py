# import sys
# input = sys.stdin.readline
#
# word1 = input().strip()
# word2 = input().strip()
#
# h, w = len(word1), len(word2)
#
# cache = [[""] * (w + 1) for _ in range(h+1)]
#
# for i in range(1, h + 1):
#     for j in range(1, w + 1):
#         if word1[i-1] == word2[j-1]:
#             cache[i][j] = cache[i-1][j-1] + word1[i-1]
#         else:
#             if len(cache[i-1][j]) < len(cache[i][j-1]):
#                 cache[i][j] = cache[i][j-1]
#             else:
#                 cache[i][j] = cache[i-1][j]
#
# print(len(cache[h][w]))
# print(cache[h][w])

import sys
input = sys.stdin.readline

word1 = input().strip()
word2 = input().strip()

h, w = len(word1), len(word2)

arr = [[0] * (w + 1) for _ in range(h+1)]

for i in range(1, h + 1):
    for j in range(1, w + 1):
        if word1[i-1] == word2[j-1]:
            arr[i][j] = arr[i-1][j-1] + 1
        else:
            if arr[i-1][j] < arr[i][j-1]:
                arr[i][j] = arr[i][j-1]
            else:
                arr[i][j] = arr[i-1][j]

print(arr[h][w])

# import sys
# input = sys.stdin.readline
#
# w1, w2 = input().strip(), input().strip()
# h, w = len(w1), len(w2)
# arr = [[0] * (w+1) for _ in range(h+1)]
#
# for i in range(1, h + 1):
#     for j in range(1, w + 1):
#         if w1[i-1] == w2[j-1]:
#             arr[i][j] = arr[i-1][j-1] + 1
#         else:
#             arr[i][j] = max(arr[i-1][j], arr[i][j-1])
# print(arr[-1][-1])

import sys

input = sys.stdin.readline

word1 = input().strip()
word2 = input().strip()

N, M = len(word1), len(word2)
cache = [0] * M

for i in range(N):
    cnt = 0
    for j in range(M):
        if cnt < cache[j]:
            cnt = cache[j]
        elif word1[i] == word2[j]:
            cache[j] = cnt + 1

print(max(cache))
