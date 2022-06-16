def solution(places):
    answer = []
    def check(graph, si, sj):
        ntc = []
        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ci, cj = si+di, sj+dj
            if 0<=ci<5 and 0<=cj<5:
                if graph[ci][cj] == 'P':
                    return False
                elif graph[ci][cj] == 'X':
                    continue
                else:
                    ntc.append((ci, cj))

        for ni, nj in ntc:
            for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                ci, cj = ni + di, nj + dj
                if ci == si and cj == sj:
                    continue
                if 0<=ci<5 and 0<=cj<5:
                    if graph[ci][cj] == 'P':
                        return False
                    else:
                        continue

        return True

    for place in places:
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    if not check(place, i, j):
                        break
            else:
                continue
            break
        else:
            answer.append(1)
            continue
        answer.append(0)

    return answer

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places))