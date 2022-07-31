import sys
import heapq
input = sys.stdin.readline


def bfs():
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True

    q = []
    heapq.heappush(q, (0, 0, 0))

    while q:
        wall, x, y = heapq.heappop(q)

        if x == n - 1 and y == m - 1:
            print(wall)
            return

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny]:
                continue

            if graph[nx][ny]:
                heapq.heappush(q, (wall + 1, nx, ny))
            else:
                heapq.heappush(q, (wall, nx, ny))
            visited[nx][ny] = True


m, n = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
bfs()
