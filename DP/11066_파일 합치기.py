import sys
input = sys.stdin.readline


T = int(input())
for _ in range(T):
    k = int(input())
    arr = list(map(int, input().split()))
    
    dp = [[0] * (k + 1) for i in range(k + 1)]
    
    for i in range(k - 1):
        dp[i][i + 1] = arr[i] + arr[i + 1]
        for j in range(i + 2, k):
            dp[i][j] = dp[i][j - 1] + arr[j]
    
    for v in range(2, k):
        for i in range(k - v):
            j = i + v
            dp[i][j] += min([dp[i][n] + dp[n + 1][j] for n in range(i, j)])
    
    print(dp[0][k - 1])
