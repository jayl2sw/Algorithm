import sys
sys.setrecursionlimit(10 ** 7)

input = sys.stdin.readline

def dfs(x):
    global ans

    visited[x] = True
    cycle.append(x)
    num = arr[x]

    if visited[num]:
        if num in cycle:
            ans += cycle[cycle.index(num):]
        return
    else:
        dfs(num)


T = int(input())
for _ in range(T):
    N = int(input())
    arr = [0] + list(map(int,input().split()))
    visited = [False] * (N + 1)
    ans = []

    for i in range(1, N+1):
        if not visited[i]:
            cycle = []
            dfs(i)

    print(N-len(ans))