import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline


def bfs(c):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    
    queue = deque()
    visited = [[-1] * n for _ in range(n)]
    for i in c:
        queue.append(virus[i])
        visited[virus[i][0]][virus[i][1]] = 0
    
    m_ = 0
    
    while queue:
        x, y = queue.popleft()
        m_ = visited[x][y]
        
        if m_ > min_:
            return -1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx <= -1 or nx >= n or ny <= -1 or ny >= n or visited[nx][ny] != -1:
                continue
            
            if graph[nx][ny] != 1:
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
    
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 1 and visited[i][j] == -1:
                return -1
        
    return m_
                

n, m = map(int, input().split())

graph = []
virus = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] == 2:
            virus.append((i, j))

min_ = float('inf')
for c in combinations(range(len(virus)), m):
    tmp = bfs(c)
    if tmp != -1:
        min_ = tmp
print(min_ if min_ != float('inf') else -1)
