import sys
from collections import deque
sys.stdin = open("data.txt", 'r')
input = sys.stdin.readline


def make_island(x, y):   
    queue = deque([(x, y)])
    visited[x][y] = True
    grid[x][y] = island
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny] or not grid[nx][ny]:
                continue
            
            queue.append((nx, ny))
            visited[nx][ny] = True
            grid[nx][ny] = island


def make_bridge(num):
    global ans
    
    visited = [[-1] * n for _ in range(n)]    
    queue = deque()
    
    for i in range(n):
        for j in range(n):
            if grid[i][j] == num:
                queue.append((i, j))
                visited[i][j] = 0
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            
            if grid[nx][ny] and grid[nx][ny] != num:
                ans = min(ans, visited[x][y])
                return
            
            if not grid[nx][ny] and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))


n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

visited = [[False] * n for _ in range(n)]

island = 0
ans = sys.maxsize

for i in range(n):
    for j in range(n):
        if grid[i][j] and not visited[i][j]:
            island += 1
            make_island(i, j)

for i in range(1, island + 1):
    make_bridge(i)

print(ans)
