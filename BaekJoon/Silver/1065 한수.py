def isHanSoo(n):
    String = str(n)
    if len(String) < 3:
        return True
    d = int(String[1]) - int(String[0])
    for i in range(len(String)-1):
        if int(String[i+1]) - int(String[i]) != d:
            return False

    return True

n = int(input())


count = 0
for i in range(1,n+1):
    if isHanSoo(i):
        count += 1

print(count)

