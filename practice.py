n, m = map(int,input().split())
def issquare(k):
    return int(k ** 0.5) ** 2 == k

nlist = []
i = 1
while i < m**0.5:
    if issquare(i):
        nlist.append(i)
    i += 1

print(nlist)

print(issquare(4))