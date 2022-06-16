from pprint import pprint

def is_bo_available(n, graph0, graph1, x, y):
    if 0 <= y-1 and graph0[x][y-1] == 0:
        return True
    elif 0 <= y-1 and x+1 <= n and graph0[x+1][y-1] == 0:
        return True
    elif 1 <= x <= n - 1 and graph1[x-1][y] == 1 and graph1[x+1][y] == 1:
        return True
    return False

def is_gi_available(n, graph0, graph1, x, y):
    if y == 0:
        return True
    elif 0 <= x-1 and graph1[x-1][y] == 1 and graph1[x][y] == 2:
        return True
    elif x + 1 <= n and graph1[x][y] == 1 and graph1[x+1][y] == 2:
        return True
    elif 0 <= y-1 and graph0[x][y-1] == 0:
        return True
    return False

def solution(n, build_frame):
    answer = []
    graph0 = [[2] * (n + 1) for _ in range(n + 1)] # 기둥 graph
    graph1 = [[2] * (n + 1) for _ in range(n + 1)] # 보 graph
    for x, y, a, b in build_frame:
        if b:
            if a:
                if is_bo_available(n, graph0, graph1, x, y):
                    graph1[x][y] = 1
            else:
                if is_gi_available(n, graph0, graph1, x, y):
                    graph0[x][y] = 0
        else:
            if a:
                graph1[x][y] = 2
                if is_bo_available(n, graph0, graph1, x+1, y) if graph1[x+1][y] else 1 and is_bo_available(n, graph0, graph1, x-1, y) if graph1[x-1][y] else 1:
                    continue
                graph1[x][y] = 1
            else:
                graph0[x][y] = 2
                if is_bo_available(n, graph0, graph1, x-1, y+1) if graph1[x-1][y+1] else 1 and is_bo_available(n, graph0, graph1, x+1, y+1) if graph1[x+1][y+1] else 1 and is_gi_available(n, graph0, graph1, x, y+1) if not graph0[x][y+1] else 1:
                    continue
                graph0[x][y] = 0

    for i in range(n+1):
        for j in range(n+1):
            if graph0[i][j] != 2:
                answer.append([i, j, graph0[i][j]])
            if graph1[i][j] != 2:
                answer.append([i, j, graph1[i][j]])

    return answer
    # print('graph1')
    # pprint(graph1)
    # print('graph0')
    # pprint(graph0)


n = 5
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]

print(solution(n, build_frame))