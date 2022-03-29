import sys

input = sys.stdin.readline

dp = [[0] * 31 for _ in range(31)]

# 알약 조각이 나오려면, 알약 하나를 꺼내서 반으로 쪼개야만 한다. 
for i in range(1, 31):
    dp[0][i] = 1

for i in range(1, 31):
    for j in range(i, 31):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

while True:
    n = int(input())

    if n == 0:
        break

    print(dp[n][n])
