import sys

sys.setrecursionlimit(10**6)
N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

def dfs(x, y, k):
    if visited[x][y]:
        return 0

    visited[x][y] = True
    cnt = 1
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and abs(board[nx][ny]-board[x][y]) <= k:
            cnt += dfs(nx, ny, k)

    return cnt

left = 0
right = 1000000
ans = 0
def is_possible(d):
    # visited 배열을 초기화합니다.
    for i in range(N):
        for j in range(N):
            visited[i][j] = False

    # 모든 구역에 대해 절반 이상이 칠해지는 구역이 있는지 확인합니다.
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                if dfs(i, j, d) * 2 >= N*N:
                    return True

    # 절반 이상이 칠해지는 구역이 없다면 False를 반환합니다.
    return False

while left <= right:
    mid = (left + right) // 2
    visited = [[False] * N for _ in range(N)]
    if is_possible(mid):
        right = mid - 1
        ans = mid
    else:
        left = mid + 1


print(ans)