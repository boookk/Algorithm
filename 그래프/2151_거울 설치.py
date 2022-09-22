"""
데이크스타 풀 때 리스트 visited에 거리를 저장한 후에 비교하지 않으면 시간 초과 발생.
"""
import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

def bfs():
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    
    sx, sy = loc[0]
    
    queue = list()
    
    for i in range(4):
        heapq.heappush(queue, (0, sx, sy, i))
        visited[sx][sy][i] = 0
    
    while queue:
        c, x, y, d = heapq.heappop(queue)

        if visited[x][y][d] < c:
            continue
        
        if x == ex and y == ey:
            print(visited[x][y][d])
            return
        
        bounds = [0, 1, 3] if grid[x][y] == '!' else [0]

        for i in bounds:
            nd = (d + i) % 4
            nx = x + dx[nd]
            ny = y + dy[nd]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= n or grid[nx][ny] == '*':
                continue

            tmp = c + (d != nd)
            if visited[nx][ny][nd] >= tmp:
                visited[nx][ny][nd] = tmp
                heapq.heappush(queue, (tmp, nx, ny, nd))


n = int(input())

grid = list()
loc = list()
visited = [[[INF] * 4 for _ in range(n)] for _ in range(n)]

for i in range(n):
    grid.append(list(input().rstrip()))
    for j in range(n):
        if grid[i][j] == '#':
            loc.append((i, j))

ex, ey = loc[1]

bfs()
