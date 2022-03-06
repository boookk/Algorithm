import sys
input = sys.stdin.readline

T = int(input())
input_list = [int(input()) for _ in range(T)]

dp = [0, 1, 1]
for i in range(3, max(input_list) + 1):
    dp.append(dp[i - 3] + dp[i - 2])

for i in input_list:
    print(dp[i])
