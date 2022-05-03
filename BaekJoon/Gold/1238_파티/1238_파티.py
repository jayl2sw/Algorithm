def dijkstra(graph):
    visited = [0] * (N + 1)
    distance = [INF] * (N + 1)
    distance[X] = 0

    while sum(visited) < len(visited) - 1:
        current_node = 0
        current_distance = INF

        for current in range(len(distance)):
            if current_distance > distance[current] and not visited[current]:
                current_node = current
                current_distance = distance[current]

        visited[current_node] = 1

        for nxt, temp in graph[current_node]:
            distance[nxt] = min(distance[nxt], distance[current_node] + temp)

    return distance

INF = int(1e9)
N, M, X = map(int,input().split())
graph1 = [[] for _ in range(N+1)]
graph2 = [[] for _ in range(N+1)]

for _ in range(M):
    start, end, dis = map(int, input().split())
    graph1[start].append((end, dis))
    graph2[end].append((start, dis))

list1 = dijkstra(graph1)
list2 = dijkstra(graph2)

result = 0
for i in range(1, N+1):
    if result < list1[i] + list2[i]:
        result = list1[i] + list2[i]
print(result)



