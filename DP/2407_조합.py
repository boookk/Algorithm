import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dp = [0] * (n + 1)
dp[1], dp[2] = 1, 2
for i in range(3, n + 1):
    dp[i] = dp[i - 1] * i

print(1 if n == m else dp[n] // (dp[m] * dp[n - m]))
