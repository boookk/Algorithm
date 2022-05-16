import sys
from collections import deque
from tkinter import W

input = sys.stdin.readline


def bfs():
    dx = [0, -1, 0, 1, 0, -1, 1, -1, 1]
    dy = [0, 0, -1, 0, 1, -1, -1, 1, 1]
    
    queue = deque([(7, 0)])
    
    while queue:
        visited = set()
        for _ in range(len(queue)):
            x, y = queue.popleft()
            
            if (x, y) in wall:
                continue
            
            if x == 0 and y == 7:
                return 1
            
            for i in range(9):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx <= -1 or nx >= 8 or ny <= -1 or ny >= 8 or (nx, ny) in visited or (nx, ny) in wall:
                    continue
                
                queue.append((nx, ny))
                visited.add((nx, ny))
        
        for _ in range(len(wall)):
            x, y = wall.popleft()
            
            if x < 7:
                wall.append((x + 1, y))
    return 0
    

graph = []
wall = deque()
for i in range(8):
    graph.append(list(input().rstrip()))
    for j in range(8):
        if graph[i][j] == '#':
            wall.append((i, j))

print(bfs())
