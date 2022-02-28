import sys
from collections import deque


def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or nx >= n or ny <= -1 or ny >= n:
                continue
            if graph[nx][ny] >= safe_zone and not visit[nx][ny]:
                visit[nx][ny] = True
                queue.append((nx, ny))


n = int(input())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
min_ = min(map(min, graph))
max_ = max(map(max, graph))

result = 1
for safe_zone in range(min_, max_ + 1):
    visit = [[False] * n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            # 안전 지대 카운팅
            if graph[i][j] >= safe_zone and not visit[i][j]:
                visit[i][j] = True
                bfs(i, j)
                count += 1
    result = max(result, count)
print(result)
