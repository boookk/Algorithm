import sys

input = sys.stdin.readline

lst = [input().rstrip() for _ in range(3)]
x, y, z = len(lst[0]), len(lst[1]), len(lst[2])

dp = [[[0 for _ in range(z + 1)] for _ in range(y + 1)] for _ in range(x + 1)]

for i in range(1, x + 1):
    for j in range(1, y + 1):
        for k in range(1, z + 1):
            if lst[0][i - 1] == lst[1][j - 1] == lst[2][k - 1]:
                dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
            else:
                dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])

result = 0
for i in range(x + 1):
    result = max(result, dp[i][y][z])
print(result)
