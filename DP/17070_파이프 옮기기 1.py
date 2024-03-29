import sys
input = sys.stdin.readline


n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dp = [[[0] * n for _ in range(n)] for _ in range(3)]
dp[0][0][1] = 1

for i in range(2, n):
    if grid[0][i] == 0:
        dp[0][0][i] = dp[0][0][i - 1]

for i in range(1, n):
    for j in range(1, n):
        if not grid[i][j] and not grid[i][j - 1] and not grid[i - 1][j]:
            dp[1][i][j] = dp[0][i - 1][j - 1] + dp[1][i - 1][j - 1] + dp[2][i - 1][j - 1]
        
        if not grid[i][j]:
            dp[0][i][j] = dp[0][i][j - 1] + dp[1][i][j - 1]
            dp[2][i][j] = dp[1][i - 1][j] + dp[2][i - 1][j]

print(sum(dp[i][n - 1][n - 1] for i in range(3)))
