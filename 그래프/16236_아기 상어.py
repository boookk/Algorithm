import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = []
fish = 0
shark_x, shark_y = 0, 0         # 아기 상어 위치
shark_size = 2
cnt = 0
ans = 0

# 아기 상어 위치와 물고기 개수 저장
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] == 9:
            shark_x, shark_y = i, j
        elif graph[i][j] != 0:
            fish += 1


def bfs(x, y):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    m_dist = float('inf')
    graph[x][y] = 0
    queue = deque([(x, y, 0)])
    visited = [[False] * n for _ in range(n)]
    visited[x][y] = True
    eat = []

    while queue:
        x, y, dist = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or nx >= n or ny <= -1 or ny >= n or visited[nx][ny]:
                continue

            if shark_size >= graph[nx][ny]:
                visited[nx][ny] = True
                if 0 < graph[nx][ny] < shark_size:
                    eat.append((nx, ny, dist + 1))
                    m_dist = dist
                if dist + 1 <= m_dist:
                    queue.append((nx, ny, dist + 1))

    if eat:
        eat.sort(key=lambda x: (x[2], x[0], x[1]))
        return eat[0]
    return False


while fish:
    result = bfs(shark_x, shark_y)
    if not result:
        break
    shark_x, shark_y = result[0], result[1]
    ans += result[2]
    cnt += 1
    graph[shark_x][shark_y] = 0
    if cnt == shark_size:
        shark_size += 1
        cnt = 0

    fish -= 1

print(ans)
