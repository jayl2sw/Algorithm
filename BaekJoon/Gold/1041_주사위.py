def least(n, array):
    if n == 1:
        return sum(sorted(array)[:-1])
    result = 0
    #1개 뽑을 때
    one_side = min(array)
    min_list = []
    min_list.append(min(array[0], array[5]))
    min_list.append(min(array[1], array[4]))
    min_list.append(min(array[2], array[3]))
    min_list.sort()
    two_side = sum(min_list[:2])
    three_side = sum(min_list)
    # corner 4개
    result += 4 * three_side
    # side 4(n-2)+ 4(n-1)개
    result += (8*n - 12) * two_side
    # 나머지 (n-2)**2 * 5
    result += (((n-2)*(n-1) * 4 + (n-2)*(n-2))* one_side)

    return result

n = int(input())
array = list(map(int,input().split()))

print(least(n, array))
