import sys
input = sys.stdin.readline


T = int(input())
input_list = [int(input()) for _ in range(T)]
dp = [1, 2, 4]
for i in range(3, max(input_list)):
    dp.append(dp[i - 1] + dp[i - 2] + dp[i - 3])
for i in input_list:
    print(dp[i - 1])
