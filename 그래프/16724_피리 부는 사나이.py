import sys
input = sys.stdin.readline


def dfs(x, y, cnt):
    global ans
    
    if visited[x][y]:
        if visited[x][y] == cnt:
            ans += 1
        return
    
    visited[x][y] = cnt
    dx, dy = d[grid[x][y]]
    nx = x + dx
    ny = y + dy
    dfs(nx, ny, cnt)


n, m = map(int, input().split())
grid = [list(input().rstrip()) for _ in range(n)]

d = {'D': (1, 0), 'U': (-1, 0), 'R': (0, 1), 'L': (0, -1)}
visited = [[0] * m for _ in range(n)]
ans = 0
cnt = 0

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            cnt += 1
            dfs(i, j, cnt)

print(ans)
