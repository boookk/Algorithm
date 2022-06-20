import sys
from collections import deque


input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

queue = deque([(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)])

for _ in range(m):
    d, s = map(int, input().split())
    visited = [[False] * n for _ in range(n)]
    
    for _ in range(len(queue)):
        x, y = queue.popleft()
        
        nx = (x + dx[d - 1] * s) % n
        ny = (y + dy[d - 1] * s) % n
        
        graph[nx][ny] += 1
        visited[nx][ny] = True
        queue.append((nx, ny))
    
    while queue:    # 물복사버그 마법
        x, y = queue.popleft()

        for i in range(1, 8, 2):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            
            if graph[nx][ny]:
                graph[x][y] += 1
    
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and graph[i][j] >= 2:
                queue.append((i, j))
                graph[i][j] -= 2

ans = 0
for i in range(n):  # 바구니에 들어있는 물의 양의 합
    for j in range(n):
        ans += graph[i][j]

print(ans)
