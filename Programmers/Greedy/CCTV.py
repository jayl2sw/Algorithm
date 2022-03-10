def solution(routes):
    cars = len(routes)
    d = [0] * 60001
    tf = [False] * cars

    for route in routes:
        start, end = route
        for i in range(d[start+30000], d[end+30000]):
            d[i] += 1

    cctvs = []
    while sum(tf) != cars:
        cctvs.append(

        )


    answer = 0
    return answer