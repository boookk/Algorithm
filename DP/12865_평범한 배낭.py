"""
참고 : https://claude-u.tistory.com/208
"""
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [[0, 0]] + [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        if j < arr[i][0]:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(arr[i][1] + dp[i - 1][j - arr[i][0]], dp[i - 1][j])

print(dp[n][k])
