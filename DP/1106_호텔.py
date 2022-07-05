import sys

input = sys.stdin.readline

c, n = map(int, input().split())
dp = [0] + [float('inf')] * (c + 100)

for _ in range(n):
    cost, customer = map(int, input().split())
    for i in range(customer, c + 101):
        dp[i] = min(dp[i], dp[i - customer] + cost)
        
print(min(dp[c:c + 101]))
