n = int(input())
array = list(map(int,input().split()))
d = [1] * n

# 왼쪽 행렬 중에 자기보다 가장 작은 수 중 가장 큰 수 의 d[i] 값보다 1 크면 된다.
for i in range(1, n):
    for j in range(i):
        if array[i] > array[j]:
            if d[i] <= d[j]:
                d[i] = d[j] + 1

print(max(d))
