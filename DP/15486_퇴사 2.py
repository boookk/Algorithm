import sys
input = sys.stdin.readline


n = int(input())

max_val = 0
dp = [0] * (n + 1)
t_list = list()
p_list = list()

for _ in range(n):
    t, p = map(int, input().split())
    t_list.append(t)
    p_list.append(p)


for i in range(n):
    max_val = max(max_val, dp[i])
    if i + t_list[i] <= n:
        dp[i + t_list[i]] = max(dp[i + t_list[i]], max_val + p_list[i])

print(max(dp))
