import sys
input = sys.stdin.readline


def dfs(idx, open1, open2):
    if idx == m:
        return 0
    
    if dp[idx][open1][open2] != -1:
        return dp[idx][open1][open2]
    
    dp[idx][open1][open2] = min(dfs(idx + 1, order[idx], open2) + abs(order[idx] - open1),
                                dfs(idx + 1, open1, order[idx]) + abs(order[idx] - open2))
    
    return dp[idx][open1][open2]


n = int(input())
open1, open2 = map(int, input().split())
m = int(input())
order = [int(input()) for _ in range(m)]

dp = [[[-1] * (n + 1) for _ in range(n + 1)] for _ in range(m)]

print(dfs(0, open1, open2))
