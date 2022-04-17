# 16진수 수를 딕셔너리로 변환할 수 있게 만들어 놓음
hx = {x: hex(x).replace('0x', '').upper() for x in range(16)}

# 10진수를 n진수로 변환하는 함수 생성
def decimalton(n, number):
    result = ''
    if number == 0:
        return '0'
    while number > 0:
        result = hx[number % n] + result
        number //= n
    return result


def solution(n, t, m, p):
    answer = ''
    number = 0
    idx = 0
    while True:
        # n진수로 바꾼 수를 일정 주기동안 answer에 넣음
        for chr in decimalton(n, number):
            # answer가 꽉차면
            if len(answer) == t:
                break
            if idx % m == p-1:
                answer += chr
            idx += 1
        else:
            number += 1
            continue
        # answer가 꽉차면 중간에 나오므로 break
        break

    return answer

print(solution(16,16,2,1))

