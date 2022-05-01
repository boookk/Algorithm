import sys
from collections import deque


def bfs():
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[0][0] = True
    queue = deque([(0, 0, 0)])

    while queue:
        x, y, cnt = queue.popleft()

        if x == y == n - 1:
            print(cnt)
            return

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or nx >= n or ny <= -1 or ny >= n or visited[nx][ny]:
                continue

            visited[nx][ny] = True
            if graph[nx][ny]:
                queue.appendleft((nx, ny, cnt))
            else:
                queue.append((nx, ny, cnt + 1))


input = sys.stdin.readline

n = int(input())
graph = [list(map(int, list(input().rstrip()))) for _ in range(n)]

bfs()
