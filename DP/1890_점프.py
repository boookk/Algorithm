import sys

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if not dp[i][j] or not graph[i][j]:
            continue
        if i + graph[i][j] < n:
            dp[i + graph[i][j]][j] += dp[i][j]
        if j + graph[i][j] < n:
            dp[i][j + graph[i][j]] += dp[i][j]

print(dp[n - 1][n - 1])
