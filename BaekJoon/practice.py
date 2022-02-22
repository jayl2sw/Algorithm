def solution(name):
    answer = 0
    arr_A = [0] * len(name)
    for i in range(len(name)):
        temp = min(ord(name[i]) - ord('A'), ord('Z') - ord(name[i]) + 1)
        answer += temp
        if name[i] == 'A':
            arr_A[i] += 1
    print(arr_A)
    return answer - 1

print(solution('JEROEN'))
print(solution('JAZ'))
