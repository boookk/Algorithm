import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return 1
    
    if visited[x][y]:
        return visited[x][y]
    
    dx, dy = d[grid[x][y]]
    nx = x + dx
    ny = y + dy
    
    visited[x][y] = -1
    visited[x][y] = dfs(nx, ny)
    
    return visited[x][y]


n, m = map(int, input().split())
grid = [list(input().rstrip()) for _ in range(n)]

visited = [[0] * m for _ in range(n)]
d = {'U': (-1, 0), 'R': (0, 1), 'D': (1, 0), 'L': (0, -1)}
answer = 0

for i in range(n):
    for j in range(m):
        if not visited[i][j] and dfs(i, j) == 1:
            answer += 1
        elif visited[i][j] == 1:
            answer += 1

print(answer)
