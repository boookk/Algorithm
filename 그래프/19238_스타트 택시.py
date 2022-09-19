import sys
from collections import deque
input = sys.stdin.readline


def bfs(x, y):
    queue = deque([(x, y)])
    
    visited[x][y] = 0
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny] != -1 or grid[nx][ny]:
                continue
            
            queue.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1


n, m, f = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
sx, sy = map(lambda x: x -1, map(int, input().split()))
customers = [list(map(lambda x: x - 1, map(int, input().split()))) for _ in range(m)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

customers_check = [False] * m

for _ in range(m):
    visited = [[-1] * n for _ in range(n)]
    bfs(sx, sy)

    for i in range(len(customers)):
        customers[i].append(visited[customers[i][0]][customers[i][1]])
    customers.sort(key= lambda x: (-x[4], -x[0], -x[1]))
    
    x, y, ex, ey, dist = customers.pop()
    customers = [customer[:-1] for customer in customers]
    
    visited = [[-1] * n for _ in range(n)]
    bfs(x, y)
    dist_ = visited[ex][ey]
    sx, sy = ex, ey
    
    if dist == -1 or dist_ == -1:
        f = -1
        break
    
    f -= dist
    if f < 0 or f < dist_:
        f = -1
        break
    
    f += dist_
    
print(f)
