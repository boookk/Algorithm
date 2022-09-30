import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m or grid[x][y] == 'H':
        return 0
    
    if visited[x][y]:
        print(-1)
        exit(0)
    
    if dp[x][y]:
        return dp[x][y]
    
    visited[x][y] = True
    
    for i in range(4):
        nx = x + dx[i] * int(grid[x][y])
        ny = y + dy[i] * int(grid[x][y])
        
        dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)
    
    visited[x][y] = False
    
    return dp[x][y]


n, m = map(int, input().split())
grid = [list(input().rstrip()) for _ in range(n)]

ans = 0
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
visited = [[False] * m for _ in range(n)]
dp = [[0] * m for _ in range(n)]

print(dfs(0, 0))
