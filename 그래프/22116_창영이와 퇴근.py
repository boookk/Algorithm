import sys
import heapq
input = sys.stdin.readline


def dijkstra():
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    visited = [[sys.maxsize] * n for _ in range(n)]
    visited[0][0] = 0

    q = []
    heapq.heappush(q, [0, 0, 0])

    while q:
        diff, x, y = heapq.heappop(q)

        if visited[x][y] < diff:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            tmp = max(diff, abs(grid[x][y] - grid[nx][ny]))
            if visited[nx][ny] > tmp:
                visited[nx][ny] = tmp
                heapq.heappush(q, [tmp, nx, ny])

    return visited[n - 1][n - 1]


n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

print(dijkstra())
