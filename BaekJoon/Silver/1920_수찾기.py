# Binary Search 문제
import sys
input = sys.stdin.readline

n = int(input())
array = sorted(map(int,input().split()))

m = int(input())
find = list(map(int, input().split()))


def binary(array, target, start, end):
    while True:
        if start > end:
            return 0
        mid = (start + end)//2
        if target == array[mid]:
            return 1
        elif target < array[mid]:
            end = mid - 1
        else:
            start = mid + 1

for i in find:
    print(binary(array, i, 0, n-1))