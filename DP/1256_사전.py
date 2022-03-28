import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
dp = [[1] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

if dp[n][m] < k:
    print(-1)
else:
    result = ''
    while True:
        if n == 0 or m == 0:
            result += n * 'a'
            result += m * 'z'
            break

        count = dp[n - 1][m]
        if k <= count:
            result += 'a'
            n -= 1
        else:
            result += 'z'
            m -= 1
            k -= count
    print(result)
