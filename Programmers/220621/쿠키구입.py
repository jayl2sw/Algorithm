def solution(cookie):
    N = len(cookie)
    for i in range(1, N):
        cookie[i] += cookie[i-1]

    cookie = [0] + cookie

    _max = 0
    for mid in range(N-1, 0, -1):
        right = N
        left = 0

        while right > mid and left < mid:
            r = cookie[right] - cookie[mid]
            l = cookie[mid] - cookie[left]
            if r < l:
                left += 1
            elif l < r:
                right -= 1
            else:
                if _max < r:
                    _max = r
                left += 1

    return _max


print(solution([1,2,4,5]))