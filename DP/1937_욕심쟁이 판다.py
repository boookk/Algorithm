import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def dfs(x, y):
    if dp[x][y] != 1:
        return dp[x][y]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx <= -1 or nx >= n or ny <= -1 or ny >= n:
            continue

        if arr[x][y] < arr[nx][ny]:
            dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)

    return dp[x][y]


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[1] * n for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

result = 0
for i in range(n):
    for j in range(n):
        result = max(result, dfs(i, j))

print(result)
