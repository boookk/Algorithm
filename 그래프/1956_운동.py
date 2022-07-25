"""
PyPy3 제출.
heapq 사용한다면 python3로 통과 가능할 것이다.
"""
import sys


input = sys.stdin.readline

v, e = map(int, input().split())
grid = [[float('inf')] * v for _ in range(v)]
for _ in range(e):
    a, b, c = map(int, input().split())
    grid[a - 1][b - 1] = c

for k in range(v):   # mid
    for i in range(v):   # from
        for j in range(v):   # to
            grid[i][j] = min(grid[i][j], grid[i][k] + grid[k][j])

ans = float('inf')
for i in range(v):
    ans = min(ans, grid[i][i])

print(-1 if ans == float('inf') else ans)
