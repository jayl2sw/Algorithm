N = int(input())
N -= 1
idx = 1
while N > 0:
    N -= 6 * idx
    idx += 1

print(idx)




