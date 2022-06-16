def solution(stones, k):
    start = 1
    end = 200000000
    answer = 0

    def check(N, stones):
        cnt = 0
        for stone in stones:
            if stone < N:
                cnt += 1
                if cnt == k:
                    return False
            else:
                cnt = 0
        return True

    while start <= end:
        mid = (start + end) // 2
        if check(mid, stones):
            start = mid + 1
            answer = mid
        else:
            end = mid - 1
    return answer

stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3

print(solution(stones, k))
