import sys
input = sys.stdin.readline


n = int(input())
scores = list(map(int, input().split()))

dp = [0] * n

for i in range(1, n):
    for j in range(1, i + 2):
        tmp = scores[i - j + 1:i + 1]
        if i + 1 == j:
            j = i
        dp[i] = max(dp[i], dp[i - j] + abs(max(tmp) - min(tmp)))

print(dp[-1])
