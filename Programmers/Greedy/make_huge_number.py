def solution(number, k):
    num = number
    answer = ''
    while k > 0:
        if not number:
            break
        first_number = max(map(int, number[:k+1]))
        front = 0
        while True:
            if int(number[front]) == first_number:
                break
            else:
                front += 1

        answer += number[front]
        number = number[front+1:]
        k -= front

    if answer == num:
        answer = answer[:(len(num)-k)]
    return answer + number


print(solution("1924", 2), "94")
print(solution("1231234", 3), "3234")
print(solution("4177252841", 4), "775841")
print(solution("99991", 3), "99")
print(solution("111119", 3), "119")
print(solution("7777777", 2), "77777")
print(solution("10000", 2), "100")
print(solution("87654321", 3), "87654")
print(solution("01010", 3), "11")