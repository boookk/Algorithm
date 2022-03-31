import sys
from collections import deque

input = sys.stdin.readline


def bfs(x, y):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    queue = deque([(x, y)])
    color = graph[x][y]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or nx >= n or ny <= -1 or ny >= n or visited[nx][ny]:
                continue

            if color == graph[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))

    return 1


n = int(input())
graph = [list(input().rstrip()) for _ in range(n)]
result = [0, 0]
visited = [[False for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            visited[i][j] = True
            result[0] += bfs(i, j)

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

visited = [[False for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            visited[i][j] = True
            result[1] += bfs(i, j)

print(*result)
