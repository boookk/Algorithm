"""
아이들의 수에서 가장 긴 증가하는 부분 수열의 길이를 빼면 해결할 수 있다.
"""
import sys

input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
dp = [1] * n

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))
