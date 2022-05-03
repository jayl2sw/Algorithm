from collections import deque

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def right_available(board, i, j, direction):
    n = len(board)
    next_d = direction+1 if direction != 3 else 0
    if 0 <= i+di[direction]+di[next_d] < n and 0 <= j+dj[direction]+dj[next_d] < n and not board[i+di[direction]+di[next_d]][j+dj[direction]+dj[next_d]] and not board[i+di[next_d]][j+dj[next_d]]:
        return True
    return False

def left_available(board, i, j, direction):
    n = len(board)
    next_d = direction-1 if direction != 0 else 3
    if 0 <= i+di[direction]+di[next_d] < n and 0 <= j+dj[direction]+dj[next_d] < n and not board[i+di[direction]+di[next_d]][j+dj[direction]+dj[next_d]] and not board[i+di[next_d]][j+dj[next_d]]:
        return True
    return False



def solution(board):
    N = len(board)
    direction = 0
    q = deque([(0,0,0,0)])
    visited = []

    while q:
        i, j, k, cost = q.popleft()
        if 0 <= i+di[k] < N and 0 <= j+dj[k] < N and i+di[k] == j+dj[k] == N-1:
            return cost
        if 0 <= i < N and 0 <= j < N and board[i+di[k]][j+dj[k]] == 0:
            if 0 <= i+2*di[k] < N and 0 <= j+2*dj[k] < N and not board[i+2*di[k]][j+2*dj[k]] and (i+di[k], j+dj[k], k) not in visited:
                q.append((i + di[k], j + dj[k], k, cost + 1))
            if right_available(board, i,j,k) and (i+di[k],j+dj[k], k+1) not in visited:
                q.append((i + di[k], j + dj[k], k+1 if k!= 3 else 0, cost + 1))
            if left_available(board, i,j,k) and (i+di[k],j+dj[k], k-1) not in visited:
                q.append((i + di[k], j + dj[k], k-1 if k != 0 else 3, cost + 1))




print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))