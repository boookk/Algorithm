import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize


def dijkstra(x, y):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    
    visited[x][y] = 0    
    q = [(0, x, y, -1)]
    
    while q:
        cnt, x, y, d = heapq.heappop(q)
        
        if visited[x][y] < cnt:
            continue
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= h or ny < 0 or ny >= w or grid[nx][ny] == '*':
                continue
            
            cost = cnt + (d != -1 and d != i)
            if cost <= visited[nx][ny]:
                heapq.heappush(q, (cost, nx, ny, i))
                visited[nx][ny] = cost
                
        


w, h = map(int, input().split())
grid = [list(input().rstrip()) for _ in range(h)]

loc = list()
visited = [[INF] * w for _ in range(h)]


for i in range(h):
    for j in range(w):
        if grid[i][j] == 'C':
            loc.append((i, j))

dijkstra(loc[0][0], loc[0][1])
print(visited[loc[1][0]][loc[1][1]] if visited[loc[1][0]][loc[1][1]] != INF else 0)
