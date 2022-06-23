# tree = [0] * 10001
#
# def intree(x):
#     idx = 1
#     while True:
#         if not tree[idx]:
#             tree[idx] = x
#             return
#         else:
#             if x > tree[idx]:
#                 idx *= 2
#                 idx += 1
#             else:
#                 idx *= 2
#
# while True:
#     try:
#         intree(int(input()))
#     except:
#         break
#
#
# idx = 1
# while idx > 0:
#     if tree[idx*2]:
#         idx *= 2
#         continue
#
#     elif tree[idx*2+1]:
#         idx *= 2
#         idx += 1
#         continue
#
#     print(tree[idx])
#     tree[idx] = 0
#     idx //= 2

import sys
sys.setrecursionlimit(10**6)
num_list=[]
while True:
    try:
        num = int(input())
        num_list.append(num)
    except:
        break

def postorder(pivot, end):
    if pivot > end:
        return
    mid = end + 1
    for i in range(pivot+1, end+1):
        if num_list[pivot] < num_list[i]:
            mid = i
            break

    postorder(pivot+1, mid-1)
    postorder(mid, end)
    print(num_list[pivot])

postorder(0, len(num_list)-1)
