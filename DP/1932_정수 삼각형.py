import sys
input = sys.stdin.readline

n = int(input())

dp = [[int(input())]]
dp += [list(map(int, input().split())) for _ in range(n-1)]

for i in range(n - 1):
    for j in range(i + 2):
        if j == 0: left = 0
        else: left = dp[i][j - 1]
        if j == i + 1: right = 0
        else: right = dp[i][j]
        dp[i + 1][j] += max(left, right)
print(max(dp[n - 1]))
