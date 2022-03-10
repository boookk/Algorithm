n = int(input())
dp = [[1] * 10] + [[0] * 10 for _ in range(n - 1)]

for i in range(1, n):
    for j in range(10):
        for k in range(j + 1):
            dp[i][j] += dp[i - 1][k]

print(sum(dp[n - 1]) % 10007)
