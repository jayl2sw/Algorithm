def solution(S):
    right = 0
    check = {S[0]:1}
    result = 1
    while right < len(S):
        if max(check.values()) > 1:
            result += 1
            check = {S[right]: 1}

        else:
            right += 1
            if right >= len(S):
                break
            if S[right] in check:
                check[S[right]] += 1
            else:
                check[S[right]] = 1
    return result

print(solution('world'))
print(solution('dddd'))
print(solution('cycle'))
print(solution('abba'))