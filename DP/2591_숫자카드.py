num = input()
n = len(num)

dp = [[0] * n for _ in range(2)]
dp[0][0] = 1

for i in range(1, n):
    if 10 <= int(num[i - 1:i + 1]) <=34:
        dp[1][i] = dp[0][i - 1]
    
    if num[i] != '0':
        dp[0][i] = dp[0][i - 1] + dp[1][i - 1]

print(dp[0][n - 1] + dp[1][n - 1])
