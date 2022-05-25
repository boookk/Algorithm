import sys

input = sys.stdin.readline

n, m = map(int, input().split())
dp = [[0] * (m + 1) for _ in range(n + 1)]
answer = 0 

for i in range(1, n + 1):
    graph = [0] + list(map(int, input().rstrip().split()))
    for j in range(1, m + 1):
        if not graph[j]:
            dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
            answer = max(answer, dp[i][j])
            
print(answer)
