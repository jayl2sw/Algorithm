# #  Longest Bitonic Subsequence
# N = int(input())
# arr = list(map(int, input().split()))
#
# dp1 = [[0]*N for _ in range(N+1)]
#
# for i in range(1, N+1):
#     for j in range(N):
#         if arr[i] < arr[j]:
#             dp1[i][j] = dp1[i-1][j-1] + 1
#         else:

# from collections import defaultdict
#
# n = int(input())
# arr = list(map(int,input().split()))
#
# left = 0
# right = 0
# d = defaultdict(int)
# d[arr[0]] += 1
# _max = 0
# while True:
#     if d[arr[right]] < 2:
#         if _max < right - left + 1:
#             _max = right - left + 1
#         right += 1
#         if right == n:
#             break
#         d[arr[right]] += 1
#     else:
#         d[arr[left]] -= 1
#         if not d[arr[left]]:
#             d.pop(arr[left])
#         left += 1
#
#
# print(_max)

n, m = map(int,input().split())

arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
flag = True
i = 0

for j in range(m):
    while i < n and arr1[i] != arr2[j]:
        i += 1

    if i == n:
        flag = False
        break
    else:
        i += 1

if flag:
    print("Yes")
else:
    print("No")





