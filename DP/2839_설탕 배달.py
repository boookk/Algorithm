import math

n = int(input())
dp = [float('inf')] * (n + 1)
dp[0] = 0
sugar = [3, 5]

for s in sugar:
    for i in range(s, n+1):
        if not math.isinf(dp[i - s]):
            dp[i] = min(dp[i], dp[i - s] + 1)

print(dp[n] if not math.isinf(dp[n]) else -1)
