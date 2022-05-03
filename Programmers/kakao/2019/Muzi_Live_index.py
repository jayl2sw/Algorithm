def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    food_times = sorted([[i, v] for i, v in enumerate(food_times, start=1)], key=lambda x: x[1])
    l =len(food_times)
    value = 0
    while k >= l:
        m = food_times[len(food_times)-l][1]
        while (m - value) * l > k:
            m -= 1

        k -= ((m-value) * l)
        value = m

        while food_times[len(food_times)-l][1] <= value:
            l -= 1



    ans = sorted([food_time for food_time in food_times if food_time[1] > value], key=lambda x: x[0])

    return ans[k][0]


food_times = [3,1,1,1,2,6]
k = 12
print(solution(food_times,k))
