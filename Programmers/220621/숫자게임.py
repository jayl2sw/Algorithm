def solution(A, B):
    A.sort(reverse=True)
    B.sort(reverse=True)

    cnt = 0
    idx = 0

    for b in B:
        while A[idx] >= b:
            idx += 1
            if idx == len(A):
                return cnt
        cnt += 1
        idx += 1
        if idx == len(A):
            return cnt

    return cnt


print(solution([5, 1, 3, 7], [2, 2, 6, 8]))
print(solution([2, 2, 2, 2], [1, 1, 1, 1]))