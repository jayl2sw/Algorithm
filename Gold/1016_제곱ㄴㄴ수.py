import sys
input = sys.stdin.readline
def solution(min,max):
    answer = max - min + 1
    check = [False] * answer
    i = 2
    while i*i <= max:
        square_number = i*i     # 제곱수

