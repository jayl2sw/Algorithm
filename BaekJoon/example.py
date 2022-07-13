import sys

sum = 0
while True:
    num = int(sys.stdin.readline().strip())
    if num < 0:
        break
    else:
       sum += num

print(sum)