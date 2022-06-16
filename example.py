# from collections import defaultdict
#
# n = int(input())
# string = input()
# d = defaultdict(int)
# _len = len(string)
# left = 0
# right = 0
# _max = 0
#
# d[string[0]] += 1
#
# while True:
#
#     if len(d) < n+1:
#         if _max < right - left + 1:
#             _max = right - left + 1
#         right += 1
#         if right == _len:
#             break
#         d[string[right]] += 1
#
#     else:
#         d[string[left]] -= 1
#         if d[string[left]] == 0:
#             del d[string[left]]
#         left += 1
# print(_max)
#

# from sortedcontainers import SortedSet
#
# n, m = map(int,input().split())
# arr = list(map(int,input().split()))
# q = []
# for _ in range(m):
#     q.append(int(input()))
#
#
# s = SortedSet(arr)
#
# for num in q:
#     idx = s.bisect_left(num)
#     if idx == len(s):
#         print(-1)
#     else:
#         print(s[idx])

# from sortedcontainers import SortedSet
#
# # 변수 선언 및 입력:
# n, m = tuple(map(int, input().split()))
# arr = list(map(int, input().split()))
# queries = [
#     int(input())
#     for _ in range(m)
# ]
#
# # treeset에 숫자들을 넣어줍니다.
# s = SortedSet(arr)
#
# # 같거나 큰 최초의 숫자를 계산합니다.
# for num in queries:
#     idx = s.bisect_left(num)
#     # 그러한 숫자가 없다면 -1을 출력합니다.
#     if idx == len(s):
#         print(-1)
#     # 존재한다면, 그 숫자를 출력합니다.
#     else:
#         print(s[idx])


from sortedcontainers import SortedSet

T = int(input())
for _ in range(T):
    n = int(input())

    s = SortedSet()
    for _ in range(n):
        command, num = input().split()
        if command == "I":
            s.add(int(num))
        elif command == 'D' and s:
            if int(num) == 1:
                s.remove(s[-1])
            else:
                s.remove(s[0])

    if not s:
        print("EMPTY")
    else:
        print(s[-1], s[0])