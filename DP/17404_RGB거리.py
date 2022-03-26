import sys

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = float('inf')

for k in range(3):
    dp = [float('inf')] * 3
    dp[k] = arr[0][k]
    for i in range(1, n):
        a = min(dp[1:]) + arr[i][0]
        b = min(dp[0], dp[2]) + arr[i][1]
        c = min(dp[:2]) + arr[i][2]
        dp = [a, b, c]

    for i in range(3):
        if i != k:
            ans = min(ans, dp[i])

print(ans)
