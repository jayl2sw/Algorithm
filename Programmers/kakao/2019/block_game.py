check = 0
answer = 0
def is_val(number, k):
    global check
    if number == k or number == 'x':
        if number == k:
            check += 1
        return True
    return False

def checking(i, j):
    global check
    global answer
    try:
        check = 0
        if is_val(board[i][j - 1], board[i][j]) and is_val(board[i][j - 2], board[i][j]):
            if is_val(board[i - 1][j - 1], board[i][j]) and is_val(board[i - 1][j], board[i][j]) and is_val(
                    board[i - 1][j - 2], board[i][j]):
                if check == 3:
                    answer += 1
                    for ci in range(i - 1, i + 1):
                        for cj in range(j - 2, j + 1):
                            board[ci][cj] = 'x'

                    for cj in range(j - 2,  j + 1):
                        for ci in range(i+1, len(board)):
                            if board[ci][j] == 0:
                                board[ci][j] = 'x'
                            else:
                                if board[ci][cj]:
                                    checking(ci, cj)
                                if i + 1 < len(board) and board[ci + 1][cj] == 0:
                                    break

                    for l in range(j - 2, j + 2):
                        checking(i+1, l)


        elif is_val(board[i][j - 1], board[i][j]):
            if is_val(board[i - 1][j], board[i][j]) and is_val(board[i - 2][j], board[i][j]) and is_val(
                    board[i - 1][j - 1], board[i][j]) and is_val(board[i - 2][j - 1], board[i][j]):
                if check == 3:
                    answer += 1
                    for ci in range(i - 2, i + 1):
                        for cj in range(j - 1, j + 1):
                            board[ci][cj] = 'x'


                    for cj in range(j - 1,  j + 1):
                        for ci in range(i, len(board)):
                            if board[ci][j] == 0:
                                board[ci][j] = 'x'
                            else:
                                if board[ci][cj]:
                                    checking(ci, cj)
                                if i + 1 < len(board) and board[ci + 1][cj] == 0:
                                    break

                    for l in range(j-2, j+3):
                        checking(i+1, l)
    except:
        pass


def solution(board):
    global check
    global answer

    for j in range(len(board[0])):
        for i in range(len(board)):
            if board[i][j] == 0:
                board[i][j] = 'x'
            else:
                if board[i][j]:
                    checking(i, j)
                if i+1 < len(board) and board[i+1][j] == 0:
                    break

    return answer

board = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,4,0,0,0],[0,0,0,0,0,4,4,0,0,0],[0,0,0,0,3,0,4,0,0,0],[0,0,0,2,3,0,0,0,5,5],[1,2,2,2,3,3,0,0,0,5],[1,1,1,0,0,0,0,0,0,5]]
print(solution(board))