import sys
input = sys.stdin.readline

TC = int(input().strip())
INF = int(1e9)

# 벨만 포드 알고리즘
def bf():
    distance = [INF] * (N+1)

    for i in range(N):
        for edge in edges:
            now, next, cost = edge

            if distance[next] > cost + distance[now]:
                distance[next] = cost + distance[now]

                if i == N - 1:
                    return True
    return False

for i in range(TC):
    N, M, W = map(int, input().split())
    edges = []

    for _ in range(M):
        S, E, T = map(int, input().split())
        edges.append((S, E, T))
        edges.append((E, S, T))

    for _ in range(W):
        S, E, T = map(int, input().split())
        edges.append((S, E, -T))


    if bf():
        print("YES")
    else:
        print("NO")
