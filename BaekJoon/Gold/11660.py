N, M = map(int,input().split())

array = [list(map(int,input().split())) for _ in range(N)]


for _ in range(M):
    si, sj, ei, ej = map(int, input().split())
