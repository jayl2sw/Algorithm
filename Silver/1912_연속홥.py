n = int(input())
array = list(map(int,input().split()))

result = [array[0]]
for i in range(1, n):
    result.append(max(array[i], result[i-1]+array[i]))

print(max(result))