from collections import deque

def bfs(board, start, end):
    visited = [[0] * 4 for _ in range(4)]
    visited[start[0]][start[1]] = 1
    q = deque([start])

    while q:
        ni, nj = q.popleft()



def solution(board, r, c):
    answer = 0

    return answer