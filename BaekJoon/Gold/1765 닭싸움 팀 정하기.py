import sys

input = lambda: sys.stdin.readline().rstrip()
def find(x):
    if mother[x] == x:
        return x
    else:
        res = find(mother[x])
        return res

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        mother[b] = a
    else:
        mother[a] = b

N = int(input())
M = int(input())

mother = list(range(N+1))
enemy = [[] for _ in range(N+1)]

for _ in range(M):
    relationship, p, q = input().split()
    p, q = int(p), int(q)
    if relationship == "E":
        for e in enemy[p]:
            union(e, q)
        for e in enemy[q]:
            union(e, p)
        enemy[p].append(q)
        enemy[q].append(p)

    else:
        union(p, q)

for i in range(len(mother)):
    mother[i] = find(mother[i])


print(len(set(mother))-1)