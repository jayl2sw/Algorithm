def solution(words):
    words.sort()
    ans = 0

    for i in range(len(words)):
        j = 0
        k = 0
        if i == 0:
            try:
                while words[i][j] == words[i + 1][j]:
                    j += 1
            except:
                j -= 1

        elif i == len(words) - 1:
            try:
                while words[i][j] == words[i - 1][j]:
                    j += 1
            except:
                pass

        else:
            try:
                while words[i][j] == words[i + 1][j]:
                    j += 1
            except:
                j -= 1  # 앞에 있는 단어를 뒤랑 비교하는 경우엔 딱 단어길이만
            try:
                while words[i][k] == words[i - 1][k]:
                    k += 1
            except:
                pass  # 뒤에 있는 단어를 앞과 비교하는 경우엔 단어길이+1 이 되게

        ans += max(j, k) + 1

    return ans