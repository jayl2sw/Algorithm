from pprint import pprint

# n은 노드 개수
# s: start


def solution(n, s, a, b, fares):
    graph = [[999999] * (n+1) for _ in range(n+1)]

    for n1, n2, cost in fares:
        graph[n1][n2] = cost
        graph[n2][n1] = cost

    for k in range(1, n+1):
        graph[k][k] = 0

    for m in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[i][j] = min(graph[i][j], graph[i][m] + graph[m][j])

    pprint(graph)
    answer = 9999999999
    for v in range(1, n+1):
        if answer > graph[s][v] + graph[v][a] + graph[v][b]:
            answer = graph[s][v] + graph[v][a] + graph[v][b]

    return answer


n = 6
s = 4
a = 6
b = 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
print(solution(n,s,a,b,fares))

