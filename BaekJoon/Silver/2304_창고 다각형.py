# n = int(input())
#
# array = [list(map(int, input().split()))for i in range(n)]
# array = sorted(array, key=lambda x: x[0])
# max_height = 0
# for i in range(len(array)):
#     if array[i][1] > max_height:
#         max_height = array[i][1]
#
#
#
# height = 0
# idx = 0
# sum = 0
# while True:
#     if height < array[idx][1]:
#         height = array[idx][1]
#     if height == max_height:
#         break
#     sum += height * (array[idx+1][0]-array[idx][0])
#     idx += 1
#
# idx = len(array) - 1
# height = 0
# while True:
#     if height < array[idx][1]:
#         height = array[idx][1]
#     if height == max_height:
#         break

#     sum += height * (array[idx][0]-array[idx-1][0]-1)
#     idx -= 1
#
# max_i = 0
# min_i = 1002
#
# for arr in array:
#     i, h = arr
#     if h == max_height:
#         if max_i < i:
#             max_i = i
#         if min_i > i:
#             min_i = i
#
# print(sum + max_height *(max_i - min_i + 1))

d = [0] * 1001
n = int(input())
for i in range(n):
    a, b = map(int,input().split())
    d[a] = b

for i in range(d.index(max(d))):
    if d[i] > d[i + 1]:
        d[i+1] = d[i]

height = 0
for j in range(1000, d.index(max(d)), -1):
    if d[j] > d[j-1]:
        d[j-1] = d[j]

print(sum(d))










