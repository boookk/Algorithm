import sys
from collections import deque


def bfs(x, y):
    dx = [-1, 0, 1, 0, -1, -1, 1, 1]
    dy = [0, -1, 0, 1, -1, 1, -1, 1]

    queue = deque([(x, y)])
    graph[x][y] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <= -1 or nx >= h or ny <= -1 or ny >= w:
                continue
            if graph[nx][ny]:
                graph[nx][ny] = 0
                queue.append((nx, ny))


result = []
while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == h == 0:
        break

    count = 0
    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                bfs(i, j)
                count += 1
    result.append(count)
print(*result, sep='\n')
