def find_mom(mother, x):
    if mother[x] != x:
        mother[x] = find_mom(mother, mother[x])
    return mother[x]


def union(mother, x, y):
    x = find_mom(mother, x)
    y = find_mom(mother, y)
    if x < y:
        mother[y] = x
    else:
        mother[x] = y


n = int(input())
m = int(input())

mother = [0] * (n + 1)

for i in range(1, n+1):
    mother[i] = i

for i in range(m):
    a, b = map(int,input().split())
    union(mother, a, b)

print(mother)

# for i in range(len(mother)):
#     if mother[i] != mother[mother[i]]:
#         mother[i] = mother[mother[i]]
#
#
# print(mother.count(1)-1)

# dfs 활용해서 풀어보기!

#
# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]
#
# def union(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     if b < a :
#         parent[a] = b
#     else:
#         parent[b] = a
#
# n = int(input())
# m = int(input())
#
# parent = [0] * (n+1)
#
# for i in range(n+1):
#     parent[i] = i
#
# for i in range(m):
#     a, b = map(int, input().split())
#     union(parent, a, b)
#
# print(mother)
#
#
#
