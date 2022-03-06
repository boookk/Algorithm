n = int(input())

dp = [[0] * 10 for _ in range(n + 1)]
for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, n + 1):
    for j in range(10):
        if j == 0:    # 10, 210 등 계단 수가 0으로 끝나는 경우
            dp[i][j] = dp[i - 1][1]
        elif j == 9:  # 계단 수가 9로 끝나는 경우
            dp[i][j] = dp[i - 1][8] 
        else:         # 계단 수가 1 ~ 8로 끝나는 경우
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

print(sum(dp[n]) % 1000000000)
