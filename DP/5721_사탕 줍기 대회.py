import sys
input = sys.stdin.readline


while True:
    n, m = map(int, input().split())
    
    if n == m == 0:
        break
    
    grid = [list(map(int, input().split())) for _ in range(n)]
    
    dp = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    
    for i in range(n):
        dp[i][0][1] = grid[i][0]
    
    for i in range(n):
        for j in range(1, m):
            dp[i][j][1] = dp[i][j - 1][0] + grid[i][j]
            dp[i][j][0] = max(dp[i][j - 1])
    
    result = [0] * n
    for i in range(n):
        tmp = 0
        for j in range(m):
            tmp = max(tmp, dp[i][j][0], dp[i][j][1])
        result[i] = tmp
    
    row = [[0] * 2 for _ in range(n)]
    row[0][1] = result[0]
    
    for i in range(1, n):
        row[i][1] = row[i - 1][0] + result[i]
        row[i][0] = max(row[i - 1])
    
    print(max(row[n - 1]))
