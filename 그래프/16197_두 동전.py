import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    
    queue = deque([coin + [0]])
    
    while queue:
        x1, y1, x2, y2, cnt = queue.popleft()

        if cnt >= 10:
            break
        
        for i in range(4):
            nx1 = x1 + dx[i]
            ny1 = y1 + dy[i]
            nx2 = x2 + dx[i]
            ny2 = y2 + dy[i]
            
            if 0 <= nx1 < n and 0 <= ny1 < m and 0 <= nx2 < n and 0 <= ny2 < m:
                if graph[nx1][ny1] == '#':
                    nx1, ny1 = x1, y1
                if graph[nx2][ny2] == '#':
                    nx2, ny2 = x2, y2
                queue.append((nx1, ny1, nx2, ny2, cnt + 1))
            elif 0 <= nx1 < n and 0 <= ny1 < m:
                return cnt + 1
            elif 0 <= nx2 < n and 0 <= ny2 < m:
                return cnt + 1
    
    return -1
                

n, m = map(int, input().split())

graph = []
coin = []
for i in range(n):
    graph.append(list(input().rstrip()))
    for j in range(m):
        if graph[i][j] == 'o':
            coin += (i, j)
            
print(bfs())
