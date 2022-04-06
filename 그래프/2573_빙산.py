import sys
from collections import deque


def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or nx >= n or ny <= -1 or ny >= m or visited[nx][ny]:
                continue

            if graph[nx][ny] != 0:
                queue.append((nx, ny))
                visited[nx][ny] = True
            else:
                count[x][y] += 1


input = sys.stdin.readline

n, m = map(int, input().split())
ans = 0
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

while True:
    bounds = 0
    visited = [[False] * m for _ in range(n)]
    count = [[0] * m for _ in range(n)]

    # 덩어리 찾기
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and graph[i][j] != 0:
                bfs(i, j)
                bounds += 1

    if bounds >= 2:
        print(ans)
        break
    if bounds == 0:
        print(0)
        break

    for i in range(n):
        for j in range(m):
            if visited[i][j]:
                graph[i][j] -= count[i][j]
                if graph[i][j] < 0:
                    graph[i][j] = 0
    ans += 1
