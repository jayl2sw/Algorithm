n, m = map(int,input().split())
times = int(input())
row = [m]
column = [n]
for _ in range(times):
    a, b= map(int,input().split())
    if a:
        column.append(b)
    else:
        row.append(b)

def max_length(array):
    result = []
    array.sort(reverse=True)
    array.append(0)

    for i in range(len(array)-1):
        result.append(array[i] - array[i+1])

    return max(result)

print(max_length(row)*max_length(column))