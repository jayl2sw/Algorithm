n = int(input())
count = 0

def checker(string):
    first = [string[0]]
    for i in range(1, len(string)):
        if string[i] == string[i-1]:
            continue
        else:
            if string[i] in first:
                return False
            else:
                first.append(string[i])


    return True

for i in range(n):
    if checker(input()):
        count += 1

print(count)






