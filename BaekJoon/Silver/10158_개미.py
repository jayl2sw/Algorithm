c, r = map(int, input().split())
x, y = map(int, input().split())
times = int(input())
# # 오른쪽 위, 왼쪽 위, 왼쪽 밑, 오른쪽 밑
# dx = True
# dy = True
#
# dx_d = [-1, 1]
# dy_d = [1, -1]
#
# while times > 0:
#     nx = x + dx_d[int(dx)]
#     ny = y + dy_d[int(dy)]
#     if nx < 0 or nx > r or ny < 0 or ny > c:
#         if nx < 0 or nx > r:
#             if dx:
#                 dx = False
#             else:
#                 dx = True
#         if ny < 0 or ny > c:
#             if dy:
#                 dy = False
#             else:
#                 dy = True
#     else:
#         x = nx
#         y = ny
#         times -= 1
#
# print(x, y)
