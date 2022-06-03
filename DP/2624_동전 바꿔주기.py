import sys

input = sys.stdin.readline

t = int(input())
k = int(input())
coin = [[0, 0]] + [list(map(int, input().split())) for _ in range(k)]

dp = [[0 for _ in range(t + 1)] for _ in range(k + 1)]
dp[0][0] = 1

for i in range(1, k + 1):
    val, cnt = coin[i]  # 동전 값, 개수
    for j in range(t + 1):
        dp[i][j] = dp[i - 1][j]
        for c in range(1, cnt + 1):
            if j - c * val >= 0:
                dp[i][j] += dp[i - 1][j - c * val]
            else:
                break

print(dp[k][t])
