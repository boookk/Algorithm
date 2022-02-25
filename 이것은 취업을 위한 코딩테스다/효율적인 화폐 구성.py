""" 다이나믹 프로그래밍 (보텀업) """
import math

n, m = map(int, input().split())
money = [int(input()) for _ in range(n)]
dp = [float('INF')] * (m + 1)

dp[0] = 0
for i in range(n):
    for j in range(money[i], m + 1):
        if not math.isinf(dp[j - money[i]]):
            dp[j] = min(dp[j], dp[j - money[i]] + 1)

if math.isinf(dp[m]):
    print(-1)
else:
    print(dp[m])
