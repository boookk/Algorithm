from collections import deque


dx = [-2, -1, -2, -1, 1, 1, 2, 2]
dy = [-1, -2, 1, 2, -2, 2, -1, 1]
T = int(input())

for _ in range(T):
    n = int(input())
    x, y = map(int, input().split())
    ax, ay = map(int, input().split())

    queue = deque([(x, y)])
    visited = [[0] * n for _ in range(n)]
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()

        if x == ax and y == ay:
            print(visited[x][y] - 1)
            break

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or nx >= n or ny <= -1 or ny >= n or visited[nx][ny]:
                continue

            queue.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1
