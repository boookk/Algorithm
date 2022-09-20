import sys
from collections import deque
input = sys.stdin.readline


def bfs(x, y):
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]

    queue = deque([(x, y)])
    
    visited[x][y] = True
    area = 1
    
    while queue:
        x, y = queue.popleft()
        wall_dir = 1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if (grid[x][y] & wall_dir) != wall_dir:
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    area += 1
                
            wall_dir *= 2
    
    return area


m, n = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

ans = [0] * 3
visited = [[False] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            ans[0] += 1
            ans[1] = max(ans[1], bfs(i, j))

for i in range(n):
    for j in range(m):
        num = 1
        while num < 9:
            if num & grid[i][j]:
                visited = [[False] * m for _ in range(n)]
                grid[i][j] -= num
                ans[2] = max(ans[2], bfs(i, j))
                grid[i][j] += num
            num *= 2

print(*ans, sep='\n')
