import sys
input = sys.stdin.readline

def solution(p, n, q):
    try:
    flag = True
    front = 0
    rear = n

    for char in p:
        if char == "R":
            flag = not flag
        else:
            if flag:
                front += 1
            else:
                rear -= 1

    if front > rear:
        return 'error'


    answer = list(q)[front:rear]
    if not flag:
        answer.reverse()

    if not answer:
        return "[]"
    answer = "["+",".join(map(str, answer))+"]"
    return answer



T = int(input().strip())

for _ in range(T):
    p = input().strip()
    n = int(input().strip())
    try:
        q = list(map(int,input()[1:-2].split(',')))
    except:
        print('error')
        continue
    print(solution(p, n, q))