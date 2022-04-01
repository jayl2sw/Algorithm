def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()

    set1 = []
    set2 = []
    for i in range(len(str1)-1):
        if ord('A') <= ord(str1[i]) <= ord('Z') and ord('A') <= ord(str1[i+1]) <= ord('Z'):
            set1.append(str1[i] + str1[i + 1])

    for i in range(len(str2) - 1):
        if ord('A') <= ord(str2[i]) <= ord('Z') and ord('A') <= ord(str2[i + 1]) <= ord('Z'):
            set2.append(str2[i] + str2[i + 1])

    set1_temp = set1[:]
    len_union = len(set1)
    for i in set2:
        if i not in set1_temp:
            len_union += 1
        else:
            set1_temp.remove(i)

    len_intersection = 0
    for i in set2:
        if i in set1:
            len_intersection += 1
            set1.remove(i)

    return int(len_intersection / len_union * 65536) if len_union else 65336


str1 = 'handshake'
str2 = 'shake hands'
print(solution(str1, str2))






