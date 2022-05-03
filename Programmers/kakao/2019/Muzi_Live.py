def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    food_times = [[i, v] for i, v in enumerate(food_times, start=1)]

    while len(food_times) <= k:
        m = min(food_times, key=lambda x: x[1])[1]
        while m * len(food_times) > k:
            m -= 1
        k -= (m * len(food_times))
        for i in range(len(food_times)):
            food_times[i][1] -= m
        n = 0
        while n < len(food_times):
            if food_times[n][1] == 0:
                food_times.remove(food_times[n])
                continue
            else:
                n += 1

    return food_times[k][0]

"""
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.1MB)
테스트 3 〉	통과 (0.02ms, 10.1MB)
테스트 4 〉	통과 (0.02ms, 10.1MB)
테스트 5 〉	통과 (0.03ms, 10.2MB)
테스트 6 〉	통과 (0.03ms, 10.2MB)
테스트 7 〉	통과 (0.03ms, 10.2MB)
테스트 8 〉	통과 (0.03ms, 10.2MB)
테스트 9 〉	통과 (0.03ms, 10.2MB)
테스트 10 〉	통과 (0.04ms, 10.2MB)
테스트 11 〉	통과 (0.04ms, 10.2MB)
테스트 12 〉	통과 (0.04ms, 10.2MB)
테스트 13 〉	통과 (0.04ms, 10.2MB)
테스트 14 〉	통과 (0.04ms, 10.2MB)
테스트 15 〉	통과 (0.04ms, 10.2MB)
테스트 16 〉	통과 (0.00ms, 10.3MB)
테스트 17 〉	통과 (0.04ms, 10.2MB)
테스트 18 〉	통과 (0.04ms, 10.2MB)
테스트 19 〉	통과 (0.00ms, 10.2MB)
테스트 20 〉	통과 (0.00ms, 10.1MB)
테스트 21 〉	통과 (0.86ms, 10.3MB)
테스트 22 〉	통과 (1.53ms, 10.1MB)
테스트 23 〉	통과 (0.00ms, 10.3MB)
테스트 24 〉	통과 (11.95ms, 10.2MB)
테스트 25 〉	통과 (4.07ms, 10.4MB)
테스트 26 〉	통과 (30.09ms, 10.4MB)
테스트 27 〉	통과 (72.81ms, 10.4MB)
테스트 28 〉	통과 (0.03ms, 10.1MB)
테스트 29 〉	통과 (0.04ms, 10.1MB)
테스트 30 〉	통과 (0.01ms, 10.2MB)
테스트 31 〉	통과 (0.01ms, 10.2MB)
테스트 32 〉	통과 (0.03ms, 10.3MB)

테스트 1 〉	실패 (시간 초과)
테스트 2 〉	통과 (113.78ms, 41.4MB)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	실패 (시간 초과)
테스트 5 〉	실패 (시간 초과)
테스트 6 〉	실패 (시간 초과)
테스트 7 〉	실패 (시간 초과)
테스트 8 〉	실패 (시간 초과)
"""