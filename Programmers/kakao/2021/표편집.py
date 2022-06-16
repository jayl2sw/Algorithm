def solution(n, k, cmd):
    answer =''
    array = list(range(n))
    pointer = k
    deleted = []

    for i in range(len(cmd)):
        if cmd[i][0] == 'U':
            pointer -= int(cmd[i][2:])
        elif cmd[i][0] == 'D':
            pointer += int(cmd[i][2:])
        elif cmd[i][0] == 'C':
            deleted.append(array.pop(pointer))
            if len(array) == pointer:
                pointer -= 1

        else:
            recently_deleted = deleted.pop()
            idx = 0
            while idx < len(array) and array[idx] < recently_deleted:
                idx += 1
            array.insert(idx, recently_deleted)

            if idx <= pointer:
                pointer += 1

    print(array)
    j = 0
    for i in range(n):
        if j < len(array) and array[j] == i:
            answer+='O'
            j += 1
        else:
            answer+='X'

    return answer




n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","C","C","C","C"]

print(solution(n, k, cmd))
# print("U 22".split())