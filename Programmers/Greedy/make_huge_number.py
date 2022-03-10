# def solution(number, k):
#     num = number
#     answer = ''
#     while k > 0:
#         if not number:
#             break
#         first_number = max(number[:k+1])
#
#         front = number.index(first_number)
#         # front = 0
#         # while int(number[front]) != int(first_number):
#         #     front += 1
#
#         answer += number[front]
#         number = number[front+1:]
#         k -= front
#
#     if answer == num:
#         answer = answer[:(len(num)-k)]
#     return answer + number


def solution(number, k):
    num = number
    answer = ''
    while k > 0:
        if not number:
            break
        first_number = max(number[:k+1])

        front = number.index(first_number)
        # front = 0
        # while int(number[front]) != int(first_number):
        #     front += 1

        answer += number[front]
        number = number[front+1:]
        k -= front

    if answer == num:
        answer = answer[:(len(num)-k)]
    return answer + number



print(solution("9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999", 40), "12")
print(solution("7777777", 3), "7777")