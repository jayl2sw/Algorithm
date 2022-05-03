import sys
input = sys.stdin.readline
def ccw(x1, y1, x2, y2, x3, y3):
    tmp = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    if tmp > 0:
        return 1
    elif tmp < 0:
        return -1
    else:
        return 0


def check(x1, y1, x2, y2, x3, y3, x4, y4):
    if ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4) == 0 and ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2) == 0:
        if min(x1, x2) <= max(x3, x4) and max(x1, x2) >= min(x3, x4) and min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2):
            return 1
    elif ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4) <= 0 and ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2) <= 0:
        return 1
        return 0


def union(a, b):
    a = find_p(a)
    b = find_p(b)

    if a < b:
        parents[b] = a
    else:
        parents[a] = b


def find_p(x):
    if parents[x] != x:
        return find_p(parents[x])
    else:
        return x


N = int(input())
parents = [0] * (N+1)
for i in range(len(parents)):
    parents[i] = i

lines = [-1]
for _ in range(N):
    lines.append(list(map(int, input().split())))

for i in range(1, N+1):
    for j in range(1, N+1):
        if i != j and parents[i] != parents[j]:
            x1, y1, x2, y2 = lines[i]
            x3, y3, x4, y4 = lines[j]
            if check(x1, y1, x2, y2, x3, y3, x4, y4):
                union(i, j)

for i in range(len(parents)):
    parents[i] = find_p(i)

counter = [0] * len(parents)
for i in range(1, N+1):
    counter[parents[i]] += 1

print(len(counter)-counter.count(0))
print(max(counter))