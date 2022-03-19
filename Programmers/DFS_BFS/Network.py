n = 4
computers = [[1, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 1], [0, 0, 1, 1]]

count = 0
v = []

def bfs(x, computers):
    global count
    global v
    q = [x]

    while q:
        now = q.pop(0)
        v.append(now)

        for nxt in range(len(computers[now])):
            if computers[now][nxt] == 1 and nxt not in q and nxt not in v:
                q.append(nxt)

    count += 1


def solution(n, computers):
    global count
    for i in range(n):
        if i not in v:
            bfs(i, computers)

    return count


print(solution(n, computers))