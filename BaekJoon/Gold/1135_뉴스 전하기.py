N = int(input())
arr = list(map(int, input().split()))

tree = [[] for _ in range(N)]

for idx in range(1, N):
    tree[arr[idx]].append(idx)

time = [0] * N

def dp(now):
    child_arr = []
    for nxt in tree[now]:
        dp(nxt)
        child_arr.append(time[nxt])
    if not tree[now]:
        child_arr.append(0)

    child_arr.sort(reverse=True)
    time[now] = max([child_arr[i]+i+1 for i in range(len(child_arr))])

dp(0)
print(time[0] - 1)