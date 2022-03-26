"""
문제 9251과 다르게 이 문제에서의 문자열은 연속된 문자여야 한다.
시간 초과가 발생하여 PyPy3로 제출하였다.
"""
import sys

input = sys.stdin.readline

s1 = input().rstrip()
s2 = input().rstrip()
n, m = len(s1), len(s2)
dp = [[0] * (m + 1) for _ in range(n + 1)]
result = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if s1[i - 1] == s2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            result = max(result, dp[i][j])

print(result)
