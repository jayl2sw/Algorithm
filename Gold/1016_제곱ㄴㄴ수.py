# 에라토스테네스의 체
import sys
input = sys.stdin.readline

def solution(min,max):
    answer = max - min + 1
    check = [False] * answer
    i = 2
    while i*i <= max:
        square = i*i     # 제곱수
        remain = 0 if min% square == 0 else 1
        j = min // square + remain
        while square * j <= max:
            if not check[square * j - min]:
                check[square * j - min] = True
                answer -= 1
            j+=1
        i+=1
    print(answer)


a, b = map(int,input().split())
solution(a,b)

