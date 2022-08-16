import sys
from collections import deque
input = sys.stdin.readline


def bfs(x, y, idx):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= r or ny < 0 or ny >= c or visited[nx][ny][idx] != -1 or grid[nx][ny] == 1:
                continue

            queue.append((nx, ny))
            visited[nx][ny][idx] = visited[x][y][idx] + 1


r, c = map(int, input().split())
grid = [list(map(int, input().rstrip())) for _ in range(r)]
# villain = [list(map(int, input().split())) for _ in range(3)]

visited = [[[-1] * 3 for _ in range(c)] for _ in range(r)]

for i in range(3):
    x, y = map(int, input().split())
    visited[x - 1][y - 1][i] = 0
    bfs(x - 1, y - 1, i)

cnt = 0
min_time = sys.maxsize
for i in range(r):
    for j in range(c):
        if min(visited[i][j][0], visited[i][j][1], visited[i][j][2]) == -1:
            continue

        tmp = max(visited[i][j][0], visited[i][j][1], visited[i][j][2])

        if min_time > tmp:
            cnt = 1
            min_time = tmp
        elif min_time == tmp:
            cnt += 1

if min_time == sys.maxsize:
    print(-1)
else:
    print(min_time)
    print(cnt)
