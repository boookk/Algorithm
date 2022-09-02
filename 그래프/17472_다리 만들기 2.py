import sys
from collections import deque
input = sys.stdin.readline


def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]


def union(a, b):
    a = find(a)
    b = find(b)

    if a == b: return False

    if a < b:
        parents[b] = a
    else:
        parents[a] = b

    return True


def bfs(x, y, k):
    queue = deque([(x, y)])
    visited[x][y] = True
    grid[x][y] = k

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny] or not grid[nx][ny]:
                continue

            queue.append((nx, ny))
            visited[nx][ny] = True
            grid[nx][ny] = k


def getEdges(x, y, k):
    queue = deque([])

    for i in range(4):
        queue.append((x, y, 0, i))

    while queue:
        x, y, dist, dir = queue.popleft()

        if grid[x][y] and grid[x][y] != k:
            if dist > 2:
                edges.add((dist - 1, k, grid[x][y]))
            continue

        nx = x + dx[dir]
        ny = y + dy[dir]

        if nx < 0 or nx >= n or ny < 0 or ny >= m or grid[nx][ny] == k:
            continue

        queue.append((nx, ny, dist + 1, dir))


n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

ans = 0
edge_cnt = 0
island_cnt = 0

visited = [[False] * m for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for i in range(n):
    for j in range(m):
        if grid[i][j] and not visited[i][j]:
            island_cnt += 1
            bfs(i, j, island_cnt)

edges = set()
parents = [i for i in range(island_cnt + 1)]

for i in range(n):
    for j in range(m):
        if grid[i][j]:
            getEdges(i, j, grid[i][j])

edges = list(edges)
edges.sort()

for cost, u, v in edges:
    if union(u, v):
        ans += cost
        edge_cnt += 1

        if edge_cnt == island_cnt - 1:
            break

print(ans if edge_cnt == island_cnt - 1 else -1)
