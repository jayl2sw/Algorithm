# String에서 조건에 맞는 Set 만들기
def makeSet(String):
    array = []
    for i in range(len(String)-1):
        if 'A' <= String[i] <= 'Z' and 'A' <= String[i+1] <= 'Z':
            array.append(String[i] + String[i + 1])

    return array

def solution(str1, str2):
    # 두개의 문자열 모두 대문자로 변환 후 Set 만듬
    set1 = makeSet(str1.upper())
    set2 = makeSet(str2.upper())

    # 1. 합집합 구하기
    set1_temp = set1[:]             # set1 copy array 생성
    len_union = len(set1)           # 합집합 개수 set1으로 초기화
    for i in set2:                  # set2 돌면서
        if i not in set1_temp:      # set1에 없으면
            len_union += 1          # 합집합 개수 하나 추가
        else:                       # set1에 있으면
            set1_temp.remove(i)     # set1 copy array 에서 해당 원소 제거

    # 2. 교집합 구하기
    set1_temp = set1[:]             # set1 copy array 생성
    len_intersection = 0            # 교집합 개수 0으로 초기화
    for i in set2:                  # set2 돌면서
        if i in set1_temp:          # set1에 있으면
            len_intersection += 1   # 교집합 개수 하나 추가
            set1.remove(i)          # set1에서 제거

    len_union = len(set1) + len(set2) - len_intersection
    return int(len_intersection / len_union * 65536) if len_union else 65536 # 만약 합집합의 개수가 0이면 65536 반환


str1 = 'handshake'
str2 = 'shake hands'
print(solution(str1, str2))






