import sys
from collections import deque


def bfs(x, y):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    cnt = 1
    graph[x][y] = 0
    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                continue

            if graph[nx][ny]:
                queue.append((nx, ny))
                graph[nx][ny] = 0
                cnt += 1

    return cnt


input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
area = 0
for i in range(n):
    for j in range(m):
        if graph[i][j]:
            area = max(area, bfs(i, j))
            cnt += 1

print(cnt)
print(area)
