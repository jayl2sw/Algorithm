def solution(s):
    min_length = 1e9
    for i in range(1, len(s)//2):
        tmp = ''
        for j in range(0, len(s), i):
            if s[j:j+i+1] == tmp[-i-1:]:
                if tmp and type(tmp[-i-2]) == int:
                    tmp = tmp[:-i-2]+ str(int(tmp[:-i-2])+1) +tmp[-i-1:]
            else:
                tmp += s[j:j+i+1]
        print(tmp)
        if len(tmp) < min_length:
            min_length = len(tmp)

    return min_length

print(solution("aabbaccc"))

