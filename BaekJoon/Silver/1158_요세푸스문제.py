n, m = map(int, input().split())

visited = [False] * (n+1)
result = []

idx = 0
while True:
    if len(result) == n:
        break



    while visited[idx]:
        idx += 1
        if idx == (n+1):
            idx = 1


    result.append(idx)
    visited[idx] = True

print(result)


