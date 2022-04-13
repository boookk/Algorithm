import sys
from collections import deque


def bfs():
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    queue = deque([(0, 0)])
    cnt = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                continue

            if not graph[nx][ny] and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = 1

            if graph[nx][ny]:
                visited[nx][ny] += 1

                if visited[nx][ny] > 1:
                    graph[nx][ny] = 0
                    cnt += 1

    return cnt


input = sys.stdin.readline
n, m = map(int, input().split())
ans = 0
graph = [list(map(int, input().split())) for _ in range(n)]

while True:
    cnt = bfs()

    if cnt:
        ans += 1
    else:
        break

print(ans)
