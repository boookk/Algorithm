import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    
    queue = deque(virus)
    
    while queue:
        v, cx, cy, time = queue.popleft()

        if time == s:
            return
        
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            
            if nx <= -1 or nx >= n or ny <= -1 or ny >= n:
                continue
            
            if not graph[nx][ny]:
                graph[nx][ny] = v
                queue.append((v, nx, ny, time + 1))
                

n, k = map(int, input().split())
graph = []
virus = []

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j]:
            virus.append((graph[i][j], i, j, 0))

s, x, y = map(int, input().split())
virus.sort()
bfs()
print(graph[x - 1][y - 1])
