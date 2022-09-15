import sys
input = sys.stdin.readline
INF = sys.maxsize


n = int(input())
m = int(input())

grid = [[False] * n for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    grid[a - 1][b - 1] = True

for k in range(n):
    for i in range(n):
        for j in range(n):
            if grid[i][k] and grid[k][j]:
                grid[i][j] = True

ans = [-1] * n
for i in range(n):
    for j in range(n):
        if not grid[i][j] and not grid[j][i]:
            ans[i] += 1

print(*ans, sep='\n')
