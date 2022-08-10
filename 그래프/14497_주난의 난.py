"""
append(), appendleft()에 따라 결과가 달라진다.
"""
import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    global ans
    
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    
    queue = deque([(x1 - 1, y1 - 1)])
    visited[x1 - 1][y1 - 1] = 0
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny] != -1:
                continue
            
            if grid[nx][ny] == '0':
                visited[nx][ny] = visited[x][y]
                queue.appendleft((nx, ny))
            else:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))


n, m = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
grid = [list(input().rstrip()) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]

bfs()
print(visited[x2 - 1][y2 - 1])
