def solution(n, k, cmd):
    answer =''
    array = [[1, i-1, i+1] for i in range(n)]
    array[-1][2]=-1
    print(array)
    pointer = k
    deleted = []

    for i in range(len(cmd)):
        if cmd[i][0] == 'U':
            for q in range(int(cmd[i][2:])):  # 주어진 숫자만큼 다음항목으로 이동
                k = array[k][2]
        elif cmd[i][0] == 'D':
            for q in range(int(cmd[i][2:])):  # 주어진 숫자만큼 다음항목으로 이동
                k = array[k][1]
        elif cmd[i][0] == "C":  # 이전 항목과 다음 항목을 잇고 삭제 큐에 추가
            nums[nums[k][0]][1] = nums[k][1]
            nums[nums[k][1]][0] = nums[k][0]
            deleted_ls.append(nums[k])
            if nums[k][1] != n:
                k = nums[k][1]
            else:
                k = nums[k][0]
        else:  # 이전항목과 다음 항목 사이에 끼어듦
            tmp = deleted_ls.pop()
            nums[tmp[0]][1] = tmp[2]
            nums[tmp[1]][0] = tmp[2]
        ans = ['O'] * n
        for q in range(len(deleted_ls)):  # 답 처리
            ans[deleted_ls[q][2]] = 'X'
        answer = ''.join(ans)
        return answer
n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","C","C","C","C"]

print(solution(n, k, cmd))