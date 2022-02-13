arr = [False] * 10001

for i in range(len(arr)):
    result = i
    while i > 0:
        result += i % 10
        i = i // 10
    if result <= 10000:
        arr[result] = True

for i in range(len(arr)):
    if not arr[i]:
        print(i)
