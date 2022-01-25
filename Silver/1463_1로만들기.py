x = int(input())

d = [0] * (x+1)


for i in range(2,x+1):
    d[i] = d[i - 1] + 1
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)

print(d[x])


"""
x = int(input())
count = 0

d = [0] * (x+1)

d[0] = int(1e9)
d[1] = 0

for i in range(2,x+1):    
    if i % 3 == 0:                              # 3으로 나눌 수 있으면 무조건 3으로 먼저 나누는 것이 이득이다.
        a3 = i//3
        d[i] = min(d[a3] + 1, d[i-1]+1)
    if i % 2 == 0:
        a2 = i//2
        d[i] = min(d[a2]+1, d[i-1]+1)
    

print(d[x])
"""