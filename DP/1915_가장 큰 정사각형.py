"""
처음에 좌표 i, j를 기준으로 dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]를 검사하여 모두 1이면 
dp[i - 1][j], dp[i][j - 1], dp[i][j] 값을 모두 갱신해주는 방식으로 풀었으나 틀렸다.
그래서 i, j를 기준으로  dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]가 모두 1이면 dp[i][j] 값만 갱신하는 방식으로 풀었다.
dp[i][j]의 값은 정사각형의 변의 길이다.
"""
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, list(input().rstrip()))) for _ in range(n)]

dp = [[0] * m for _ in range(n)]

result = 0
for i in range(n):
    for j in range(m):
        if i == 0 or j == 0:
            dp[i][j] = arr[i][j]
        elif arr[i][j]:
            dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        result = max(result, dp[i][j])

print(result ** 2)
