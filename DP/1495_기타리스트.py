import sys           

input = sys.stdin.readline

n, s, m = map(int, input().split())
lst = list(map(int, input().split()))

dp = [[False] * (m + 1) for _ in range(n + 1)]
dp[0][s] = True

for i in range(n):
    for j in range(m + 1):
        if dp[i][j]:
            if j + lst[i] <= m:
                dp[i + 1][j + lst[i]] = True
            if j - lst[i] >= 0:
                dp[i + 1][j - lst[i]] = True

ans = -1
for i in range(m, -1, -1):
    if dp[n][i]:
        ans = i
        break

print(ans)
