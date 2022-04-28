import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    dx = [-1, 0, 1, 0, 0, 0]
    dy = [0, -1, 0, 1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]
    
    visited = [[[0] * c for _ in range(r)] for _ in range(l)]
    
    queue = deque([point[0]])
    
    while queue:
        z, x, y = queue.popleft()
        
        if graph[z][x][y] == 'E':
            return f'Escaped in {visited[z][x][y]} minute(s).'
        
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            
            if nx <= -1 or nx >= r or ny <= -1 or ny >= c or nz <= -1 or nz >= l or visited[nz][nx][ny]:
                continue
            
            if graph[nz][nx][ny] == '.' or graph[nz][nx][ny] == 'E':
                visited[nz][nx][ny] = visited[z][x][y] + 1
                queue.append([nz, nx, ny])

    return 'Trapped!'


while True:
    l, r, c = map(int, input().split())

    if l == 0:
        break
    
    point = [[] for _ in range(2)]  # 현재 위치, 탈출 지점
    graph = list()
    
    for k in range(l):
        tmp = [list(input().rstrip()) for _ in range(r)]
        input()
        
        for i in range(r):
            for j in range(c):
                if tmp[i][j] == 'S':
                    point[0] = [k, i, j]
                elif tmp[i][j] == 'E':
                    point[1] = [k, i, j]
        
        graph.append(tmp)
    
    print(bfs())
