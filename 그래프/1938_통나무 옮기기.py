import sys
from collections import deque
input = sys.stdin.readline


def move(x, y, d, nd):
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    
    if nd == 4:
        if 1 <= x < n - 1 and 1 <= y < n - 1:
            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    if grid[i][j] == '1':
                        return (x, y, d)
            return (x, y, 1 - d)
    else:
        nx = x + dx[nd]
        ny = y + dy[nd]
        
        if d:
            if 1 <= nx < n - 1 and 0 <= ny < n:
                if grid[nx - 1][ny] != '1' and grid[nx][ny] != '1' and grid[nx + 1][ny] != '1':
                    return (nx, ny, d)
        else:
            if 0 <= nx < n and 1 <= ny < n - 1:
                if grid[nx][ny - 1] != '1' and grid[nx][ny] != '1' and grid[nx][ny + 1] != '1':
                    return (nx, ny, d)
    
    return (x, y, d)


def bfs():    
    visited = set()
    visited.add(tree)
    
    queue = deque([(tree[0], tree[1], tree[2], 0)])

    while queue:
        x, y, d, cnt = queue.popleft()
        
        for i in range(5):
            nx, ny, nd = move(x, y, d, i)
            
            if (nx, ny, nd) not in visited:
                if (nx, ny, nd) == target:
                    return cnt + 1
                visited.add((nx, ny, nd))
                queue.append((nx, ny, nd, cnt + 1))

    return 0


n = int(input())

grid = [list(input().rstrip()) for _ in range(n)]
tree = set()
target = set()

for i in range(n):
    for j in range(n):
        if not len(tree) and grid[i][j] == 'B':
            if i + 1 < n and grid[i + 1][j] == 'B': # 세로
                tree = (i + 1, j, 1)
                for k in range(3):
                    grid[i + k][j] = '0'
            else:
                tree = (i, j + 1, 0)
                for k in range(3):
                    grid[i][j + k] = '0'
        elif not len(target) and grid[i][j] == 'E':
            if i + 1 < n and grid[i + 1][j] == 'E': # 세로
                target = (i + 1, j, 1)
            else:
                target = (i, j + 1, 0)

print(bfs())
