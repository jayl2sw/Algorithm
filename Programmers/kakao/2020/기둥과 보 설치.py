from pprint import pprint

def solution(n, build_frame):
    graph = [[2] * (n+1) for _ in range(n+1)]
    answer = []
    for frame in build_frame:
        x, y, a, b = frame
        if b:
            if a:
                if not graph[x][y-1]:
                    graph[x][y] = 1
                elif not graph[x+1][y-1]:
                    graph[x][y] = 1
                elif graph[x-1][y] == 1 and graph[x+1][y] == 1:
                    graph[x][y] = 1
            else:
                if y == 0:
                    graph[x][y] = 0
                elif graph[x-1][y] == 1 and graph[x][y] == 2:
                    graph[x][y] = 0
                elif graph[x][y-1] == 0:
                    graph[x][y] = 0
                elif graph[x][y] == 1:
                    graph[x][y] = 0
        else:
            
            graph[x][y] = 2
    pprint(graph)
    for i in range(n+1):
        for j in range(n+1):
            if graph[i][j] != 2:
                answer.append([i, j, graph[i][j]])
                if graph[i][j] == 0 and j-1 > 0:
                    if graph[i+1][j] == 1 or graph[i+1][j-1] == 0:
                        answer.append([i, j, 1])

    pprint(graph)



    return answer


n = 5
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]

print(solution(n, build_frame))