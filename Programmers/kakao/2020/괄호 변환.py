# from collections import deque
#
# def check(brackets):
#     idx = 0
#     temp = 0
#     while temp >= 0 and idx < len(brackets):
#         if brackets[idx] == '(':
#             temp += 1
#         else:
#             temp -= 1
#         idx += 1
#     if idx == len(brackets):
#         return True
#     else:
#         return False
#
#
# def solution(p):
#     answer = ''
#     if not p:
#         return answer
#
#     v = deque(p)
#
#     while v:
#         n = 0
#         balance = 0
#         u = ''
#
#         while n == 0 or balance != 0 and v:
#             tmp = v.popleft()
#             u += tmp
#             if tmp == '(':
#                 balance += 1
#             else:
#                 balance -= 1
#             n += 1
#
#         # v에 대해 1단계부터 재귀적으로 수행하면 "()"이 반환됩니다.
#         if check(u):
#             answer += u
#         else:
#             temp = '(' + solution(v) + ')'
#             for bracket in u[1:len(temp)-1]:
#                 if bracket == '(':
#                     temp += ')'
#                 else:
#                     temp += '('
#
#             answer += temp
#             v = ''
#     return answer
#
#
# print(solution("()))((()"))
#
def check(brackets):
    idx = 0
    temp = 0
    while temp >= 0 and idx < len(brackets):
        if brackets[idx] == '(':
            temp += 1
        else:
            temp -= 1
        idx += 1
    if idx == len(brackets):
        return True
    else:
        return False


from collections import deque

def solution(p):
    answer = ''
    if not p:
        return answer

    v = deque(p)

    while v:
        n = 0
        balance = 0
        u = ''

        while n == 0 or balance != 0 and v:
            tmp = v.popleft()
            u += tmp
            if tmp == '(':
                balance += 1
            else:
                balance -= 1
            n += 1

        if check(u):
            answer += u
        else:
            break
    else:
        return answer

    temp = '(' + solution(v) + ')'
    for bracket in u[1:len(u)-1]:
        if bracket == '(':
            temp += ')'
        else:
            temp += '('


    answer += temp
    return answer

print(solution("()))()((()"))