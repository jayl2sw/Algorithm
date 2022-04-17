# 2022-04-03 프로그래머스 뉴스 클러스터링
# 시작 20:40
# 제출 20:51
from collections import defaultdict


def solution(str1, str2):
    str1 = str_to_lst(str1.upper())
    str2 = str_to_lst(str2.upper())
    n = sum(str1.values())
    m = sum(str2.values())
    if n == m == 0:
        return 65536
    cnt = 0
    for s1 in str1:
        cnt += min(str1[s1], str2[s1])
    return int((cnt / (n + m - cnt)) * 65536)


def str_to_lst(my_str):
    l = len(my_str)
    result = defaultdict(int)
    for i in range(1, l):
        if check_abc(my_str[i - 1]) and check_abc(my_str[i]):
            result[my_str[i - 1:i + 1]] += 1
            print(result)
    return result


def check_abc(my_str):
    if 'A' <= my_str <= 'Z':
        return True
    return False


str1 = 'handshake'
str2 = 'shake hands'
print(solution(str1, str2))

