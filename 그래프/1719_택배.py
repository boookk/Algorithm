import sys
input = sys.stdin.readline
INF = sys.maxsize

n, m = map(int, input().split())

dist = [[0 if i == j else INF for j in range(n + 1)] for i in range(n + 1)]
result = [[i for i in range(n + 1)] for _ in range(n + 1)]

for _ in range(m):
    u, v, cost = map(int, input().split())
    dist[u][v] = cost
    dist[v][u] = cost

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                result[i][j] = '-'
                continue
            tmp = dist[i][k] + dist[k][j]
            if dist[i][j] > tmp:
                dist[i][j] = tmp
                result[i][j] = result[i][k]

for row in result[1:]:
    print(*row[1:])
