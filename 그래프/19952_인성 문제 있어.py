import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    queue = deque([(sx - 1, sy - 1, f)])

    visited = [[False] * w for _ in range(h)]
    visited[sx - 1][sy - 1] = True

    while queue:
        x, y, power = queue.popleft()

        if x == ex - 1 and y == ey - 1:
            return "잘했어!!"

        if not power:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= h or ny < 0 or ny >= w or visited[nx][ny]:
                continue

            if grid[nx][ny] - grid[x][y] <= power:
                visited[nx][ny] = True
                queue.append((nx, ny, power - 1))

    return "인성 문제있어??"


T = int(input())
for _ in range(T):
    h, w, o, f, sx, sy, ex, ey = map(int, input().split())

    grid = [[0] * w for _ in range(h)]

    for _ in range(o):
        x, y, l = map(int, input().split())
        grid[x - 1][y - 1] = l

    print(bfs())
