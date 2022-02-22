n = int(input())

array = []
for i in range(n):
    array.append(list(map(int,input().split())))


for i in range(n-1):
    for j in range(n-i-1):
        array[-2-i][j] += max(array[-1-i][j],array[-1-i ][j+1])

print(array[0][0])