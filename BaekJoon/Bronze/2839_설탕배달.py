n = int(input())

def sugar(n):
    count = 0
    while n % 5 != 0:
        if n < 2:
            return -1
        n -= 3
        count += 1

    count += int(n/5)
    return count

print(sugar(n))
