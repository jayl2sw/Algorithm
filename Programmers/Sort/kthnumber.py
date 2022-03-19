def solution(array, commands):
    answer = []
    for command in commands:
        start, end, k = command
        temp = sorted(array[start-1: end])
        answer.append(temp[k-1])

    return answer


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
result = [5, 6, 3]
print(solution(array, commands))