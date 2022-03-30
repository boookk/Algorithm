import sys

input = sys.stdin.readline

dp = [[1 for _ in range(10)] for _ in range(65)]

for i in range(1, 65):
    for j in range(1, 10):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

T = int(input())
for _ in range(T):
    n = int(input())
    print(dp[n][-1])
