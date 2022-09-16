"""
PyPy3 제출
"""
import sys
input = sys.stdin.readline


n, m = map(int, input().split())

grid = [[False] * n for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    grid[a - 1][b - 1] = True

for k in range(n):
    for i in range(n):
        for j in range(n):
            if grid[i][k] and grid[k][j]:
                grid[i][j] = True

s = int(input())
for _ in range(s):
    a, b = map(int, input().split())
    if grid[a - 1][b - 1]:
        print(-1)
    elif grid[b - 1][a - 1]:
        print(1)
    elif not grid[a - 1][b - 1]:
        print(0)
