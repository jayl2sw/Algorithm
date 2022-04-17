from collections import deque

s, t = map(int, input().split())
q = deque()
check = set()
q.append((s, ''))
MAX = int(1e9)

if s ==t :
    print(0)
else:
    result = -1
    while q:
        s, result = q.popleft()
        if s == t:
            print(result)
            break

        nxt = s * s

        if 0 <= nxt <= MAX and nxt not in check:
            q.append((nxt, result+'*'))
            check.add(nxt)

        nxt = s + s
        if 0 <= nxt <= MAX and nxt not in check:
            q.append((nxt, result + '+'))
            check.add(nxt)

        nxt = 1
        if nxt not in check:
            q.append((nxt, result + '/'))
            check.add(nxt)
    else:
        print(-1)