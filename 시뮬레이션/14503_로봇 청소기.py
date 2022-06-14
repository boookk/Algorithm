import sys


input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visited = [[False for _ in range(m)] for _ in range(n)]
visited[r][c] = True

ans = 1     # 청소한 칸 카운팅

while True:

    for _ in range(4):
        d = (d + 3) % 4
        nx = r + dx[d]
        ny = c + dy[d]

        if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny] or graph[nx][ny]:
            continue

        ans += 1
        r, c = nx, ny
        visited[nx][ny] = True
        break
    else:

        d_ = d + 2 if d in [0, 1] else d - 2

        r = r + dx[d_]
        c = c + dy[d_]

        if graph[r][c]:
            break

print(ans)
