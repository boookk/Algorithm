import sys

input = sys.stdin.readline

t, w = map(int, input().split())
graph = [int(input()) for _ in range(t)]
dp = [[0 for _ in range(w + 1)] for _ in range(t)]

for i in range(t):
    for j in range(w + 1):
        if  j == 0:
            dp[i][0] = dp[i - 1][0] + 1 if graph[i] == 1 else dp[i - 1][0]
        else:
            if graph[i] == 1 and j % 2 == 0:
                dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + 1
            elif graph[i] == 2 and j % 2 == 1:
                dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + 1
            else:
                dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j])

print(max(dp[t - 1]))
