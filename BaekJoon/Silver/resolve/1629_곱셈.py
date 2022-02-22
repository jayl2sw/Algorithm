a, b, c = map(int, input().split())


def dfs(a, n):
    if n == 1:
        return a % c

    temp = dfs(a, n // 2)
    if n % 2:
        return (temp ** 2 * a) % c
    else:
        return temp ** 2 % c


print(dfs(a, b))
