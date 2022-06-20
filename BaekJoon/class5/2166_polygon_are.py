import sys
input = sys.stdin.readline

N = int(input().strip())

standard = list(map(int,input().split()))
points = [list(map(int,input().split())) for _ in range(N-1)]

answer = 0

for i in range(1, len(points)):
    p1 = points[i-1]
    p2 = points[i]
    answer += (abs((standard[0] * p1[1] + p1[0] * p2[1] + p2[0] * standard[1])-(standard[1] * p1[0] + p1[1] * p2[0] + p2[1] * standard[0])) // 2)

print(answer)






