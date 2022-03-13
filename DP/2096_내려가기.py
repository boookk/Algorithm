import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
min_dp = arr
max_dp = arr

for i in range(n - 1):
    a, b, c = map(int, input().split())
    max_dp = [max(max_dp[:2]) + a, max(max_dp) + b, max(max_dp[1:]) + c]
    min_dp = [min(min_dp[:2]) + a, min(min_dp) + b, min(min_dp[1:]) + c]

print(max(max_dp), min(min_dp))
