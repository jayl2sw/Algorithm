def solution(board, skill):
    answer = 0
    d = [[0]*(len(board[0])+1) for _ in range(len(board)+1)]

    for tp, r1, c1, r2, c2, degree in skill:
        if tp == 1:
            d[r1][c1] -= degree
            d[r1][c2 + 1] += degree
            d[r2 + 1][c1] += degree
            d[r2 + 1][c2 + 1] -= degree

        if tp == 2:
            d[r1][c1] += degree
            d[r1][c2+1] -= degree
            d[r2+1][c1] -= degree
            d[r2+1][c2+1] += degree

    for i in range(len(d)-1):
        for j in range(len(d[0])-1):
            d[i][j + 1] += d[i][j]

    for j in range(len(d[0]) - 1):
        for i in range(len(d) - 1):
            d[i + 1][j] += d[i][j]

    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += d[i][j]
            if board[i][j] > 0:
                answer += 1

    return answer

board = [[1,2,3],[4,5,6],[7,8,9]]
skill = [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]
print(solution(board, skill))

테스트 1 〉	통과 (877.27ms, 143MB)
테스트 2 〉	통과 (881.59ms, 143MB)
테스트 3 〉	통과 (878.06ms, 143MB)
테스트 4 〉	통과 (768.95ms, 143MB)
테스트 5 〉	통과 (644.95ms, 132MB)
테스트 6 〉	통과 (671.98ms, 132MB)
테스트 7 〉	통과 (688.01ms, 132MB)