def subset_sum(n, s, array):
    result = 0
    for i in range(1, 1 << n):
        sub_sum = 0
        for j in range(n):
            if i & (1 << j):
                sub_sum += array[j]
        if sub_sum == s:
            result += 1
    return result

n, s = map(int,input().split())
array = list(map(int,input().split()))

print(subset_sum(n, s, array))