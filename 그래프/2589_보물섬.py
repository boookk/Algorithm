"""
브루트 포스 알고리즘으로 풀기 위해 모든 구간을 탐색하며, 섬이라면 해당 섬에서 가장 먼 섬을 구한다.
python으로 시간 초과가 발생하여 PyPy3로 제출했다.
"""
import sys
from collections import deque


def bfs(x, y):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    visited = [[-1] * m for _ in range(n)]
    visited[x][y] = 0
    queue = deque([(x, y)])
    dist = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                continue

            if graph[nx][ny] == 'L' and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                dist = max(dist, visited[nx][ny])
                queue.append((nx, ny))

    return dist


input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]

ans = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            ans = max(ans, bfs(i, j))
            
print(ans)
