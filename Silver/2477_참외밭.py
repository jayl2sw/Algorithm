n = int(input())
array = [-1, 3, 4, 2, 1]

side = []
length = []
for i in range(6):
    a, b = map(int,input().split())
    side.append(a)
    length.append(b)

side.append(side[0])

for idx in range(6):
    if array[side[idx]] == side[idx + 1]:
        void = idx
void2 = (void + 1) % 6
x = length[(void + 3) % 6]
y = length[(void + 4) % 6]

total = x * y
empty = length[void] * length[void2]
length.sort()

print((total - empty) * n)