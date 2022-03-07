import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]

    dp = [[0] * n for _ in range(2)]
    dp[0][0], dp[1][0] = arr[0][0], arr[1][0]

    if n > 1:
        dp[0][1] = max(arr[1][0] + arr[0][1], arr[0][0])
        dp[1][1] = max(arr[0][0] + arr[1][1], arr[1][0])

    for j in range(2, n):
        for i in range(2):
            if i: dp[i][j] = max(dp[1][j - 1], arr[i][j] + dp[0][j - 1])
            else: dp[i][j] = max(dp[0][j - 1], arr[i][j] + dp[1][j - 1])

    print(max(dp[0][n - 1], dp[1][n - 1]))
