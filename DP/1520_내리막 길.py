"""
DP + DFS 문제다.
Python으로 풀면 재귀호출 횟수를 초과하지만, PyPy3로 제출하면 통과한다.
"""

import sys

input = sys.stdin.readline


def dfs(x, y):
    if n - 1 == x and m - 1 == y:
        return 1

    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
            continue

        if arr[x][y] > arr[nx][ny]:
            dp[x][y] += dfs(nx, ny)

    return dp[x][y]


dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[-1] * m for _ in range(n)]

print(dfs(0, 0))
