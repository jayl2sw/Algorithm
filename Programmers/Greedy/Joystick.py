def judge(name):
    vertical = len(name) - 1

    if 'A' in name:
        last_A_index = len(name) - name[::-1].index('A')
        behind = len(name) - last_A_index

        for i in range(len(name)):
            if name[-1-i] != 'A':
                behind_As = i

        if behind_As == 0:
            for i in range(len(name)):
                if name[i+1] == 'A':
                    if min(behind + i,  len(name) - behind_As - i - 1) == behind + i:
                        result = behind + i
                        break
        else:
            for i in range(len(name)):
                if name[i+1] == 'A':
                    if min(len(name) - behind_As - i - 1) == behind + i:
                        result = behind
                        break






def solution(name):
    answer = 0
    for i in range(len(name)):
        answer += min(ord(name[i]) - ord('A'), ord('Z') - ord(name[i]) + 1)

    # vertical = len(name) - 1
    #
    # if 'A' in name:
    #     last_A_index = len(name) - name[::-1].index('A')
    #     behind = len(name) - last_A_index
    #
    #     re_idx = 0
    #     if not last_A_index:
    #         while True:
    #             if name[::-1][re_idx + 1]:
    #                 re_idx += 1
    #             else:
    #                 break
    #
    #     for j in range(len(name)):
    #         if name[j+1] == 'A':
    #             if min(len(name) - re_idx - j - 1, behind + j) == behind + j:
    #                 vertical = behind + j
    #                 break
    #             else:
    #                 continue
    #
    # answer += vertical



    return answer


print(solution('JEROEN'))