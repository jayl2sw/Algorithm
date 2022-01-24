import math

a, b, v= map(int,input().split())

count = 0
rest = v - a
in_day = a - b
count = math.ceil(rest / in_day) + 1
print(count)