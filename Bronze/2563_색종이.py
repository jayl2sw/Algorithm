n = int(input())
paper = [([0] * 101) for _ in range(101)]

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            paper[x+i][y+j] += 1

total = 0
for a in range(101):
    for b in range(101):
        if paper[a][b] >= 1:
            total += 1

print(total)



