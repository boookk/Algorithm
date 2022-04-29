"""
방문 체크를 어떻게 하는지 중요 !
"""
import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    
    while queue:
        x, y = queue.popleft()
        
        if graph[x][y] == 'J' and (x == 0 or x == r - 1 or y == 0 or y == c - 1):
            return visited[x][y] + 1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx <= -1 or nx >= r or ny <= -1 or ny >= c:
                continue
            
            if graph[x][y] == 'J' and graph[nx][ny] == '.' and visited[nx][ny] == -1:
                graph[nx][ny] = 'J'
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
            if graph[x][y] == 'F' and graph[nx][ny] != '#' and visited[nx][ny] != 0:
                graph[nx][ny] = 'F'
                queue.append((nx, ny))
                visited[nx][ny] = 0

    return 'IMPOSSIBLE'


r, c = map(int, input().split())
graph = []
queue = deque()
visited = [[-1] * c for _ in range(r)]

for i in range(r):
    graph.append(list(input().rstrip()))
    for j in range(c):
        if graph[i][j] == 'J':
            queue.appendleft((i, j))
            visited[i][j] = 0
        elif graph[i][j] == 'F':
            queue.append((i, j))
            visited[i][j] = 0

print(bfs())
