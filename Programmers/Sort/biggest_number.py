

def solution(numbers):
    answer=' '
    sort_number = sorted(numbers, key=lambda x: ('{0:0<4}'.format(x)[0], '{0:0<4}'.format(x)[1], '{0:0<4}'.format(x)[2], '{0:0<4}'.format(x)[3]), reverse=True)
    for number in sort_number:
        answer += str(number)
    return answer



numbers = [6, 12, 1000,10, 2,]


print(solution(numbers))