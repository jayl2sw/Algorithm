n = int(input())

total_r = 0
total_g = 0
total_b = 0

for i in range(n):
    r, g, b = map(int,input().split())
    total_r, total_g, total_b = r + min(total_g, total_b), g+min(total_r, total_b),b+ min(total_g, total_r)


print(min(total_r, total_b, total_g))