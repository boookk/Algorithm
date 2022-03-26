"""
DP + BFS 로 풀어야 하는 문제다.
화면에 있는 이모티콘 개수와 클립보드에 있는 이모티콘 개수를 각각을 x, y로 생각하고
dp 테이블에 x, y에 시간을 저장한다.
"""
import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    queue = deque([(1, 0)])

    while queue:
        x, y = queue.popleft()

        if dp[x][x] == -1:
            dp[x][x] = dp[x][y] + 1
            queue.append((x, x))
        if x + y <= n and dp[x + y][y] == -1:
            dp[x + y][y] = dp[x][y] + 1
            queue.append((x + y, y))
        if x - 1 >= 0 and dp[x - 1][y] == -1:
            dp[x - 1][y] = dp[x][y] + 1
            queue.append((x - 1, y))


n = int(input())
dp = [[-1] * (n + 1) for _ in range(n + 1)]
dp[1][0] = 0
bfs()
print(min(filter(lambda x: x != -1, dp[n])))
