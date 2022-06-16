import sys
input = sys.stdin.readline

word1 = input().strip()
word2 = input().strip()

h, w = len(word1), len(word2)

arr = [[""] * (w + 1) for _ in range(h+1)]

for i in range(1, h + 1):
    for j in range(1, w + 1):
        if word1[i-1] == word2[j-1]:
            arr[i][j] = arr[i-1][j-1] + word1[i-1]
        else:
            if len(arr[i-1][j]) < len(arr[i][j-1]):
                arr[i][j] = arr[i][j-1]
            else:
                arr[i][j] = arr[i-1][j]

print(len(arr[h][w]))
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