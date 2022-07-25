N = int(input())

def compare(a, b):
    i1, w1, h1 = a
    i2, w2, h2 = b

    if w1 > w2 and h1 > h2:
        rank[i2] += 1
    elif w2 > w1 and h2 > h1:
        rank[i1] += 1

arr = []
rank = [1] * N

for i in range(N):
    weight, height = map(int,input().split())
    arr.append((i, weight, height))

for i in range(N):
    for j in range(i+1, N):
        compare(arr[i], arr[j])

print(" ".join(map(str, rank)))
