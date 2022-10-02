import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline


def dfs(u):
    visited[u] = True
    dp[u][0] = 1
    
    for v in graph[u]:
        if not visited[v]:
            dfs(v)
            dp[u][0] += min(dp[v][0], dp[v][1])
            dp[u][1] += dp[v][0]


n = int(input())

graph = [[] for _ in range(n)]
visited = [False] * n
dp = [[0, 0] for _ in range(n)]

for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)

dfs(0)
print(min(dp[0]))
