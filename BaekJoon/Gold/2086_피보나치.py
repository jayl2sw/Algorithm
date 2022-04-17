a, b = map(int,input().split())
start = 0
mid = 1
for i in range(1, b):
    temp = start + mid + 1
    if i == a-2:
        t = temp
    start, mid = mid, temp
print(temp-t)


.mode csv
.imort users.csv users_user