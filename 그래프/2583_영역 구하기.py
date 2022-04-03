import sys
from collections import deque


def bfs(x, y):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    count = 1
    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or nx >= m or ny <= -1 or ny >= n:
                continue

            if not grid[nx][ny]:
                queue.append((nx, ny))
                count += 1
                grid[nx][ny] = 1
    return count


input = sys.stdin.readline

m, n, k = map(int, input().split())
grid = [[0 for _ in range(n)] for _ in range(m)]
for _ in range(k):
    lx, ly, rx, ry = map(int, input().split())
    h_start, h_end = m - ry, m - ly
    w_start, w_end = lx, rx

    for h in range(h_start, h_end):
        for w in range(w_start, w_end):
            grid[h][w] = 1

ans = []
for i in range(m):
    for j in range(n):
        if not grid[i][j]:
            grid[i][j] = 1
            ans.append(bfs(i, j))

print(len(ans))
print(*sorted(ans))
