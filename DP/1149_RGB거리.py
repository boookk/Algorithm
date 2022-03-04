import sys
input = sys.stdin.readline
n = int(input())
dp = [list(map(int, input().split())) for _ in range(n)]
for i in range(1, n):
    # i번째 집을 빨간색으로 칠할 경우, i - 1번째 집은 초록, 파랑 중 작은 값으로 페인팅
    dp[i][0] += min(dp[i - 1][1], dp[i - 1][2])
    # i번쨰 집을 초록색으로 칠할 경우, i - 1번째 집은 빨강, 파랑 중 작은 값으로 페인팅
    dp[i][1] += min(dp[i - 1][0], dp[i - 1][2])
    # i번째 집을 파랑색으로 칠할 경우, i - 1번째 집은 빨강, 초록 중 작은 값으로 페인팅
    dp[i][2] += min(dp[i - 1][0], dp[i - 1][1])
print(min(dp[n - 1]))
