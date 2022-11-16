import sys
from collections import deque
input = sys.stdin.readline


def bfs(y, x):
    queue = deque([(y, x)])
    visited[y][x] = 1
    
    while queue:
        y, x = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx <= 2000 and 0 <= ny <= 2000 and not visited[ny][nx] and maps[ny][nx]:
                visited[ny][nx] = 1
                queue.append((ny, nx))


n = int(input())

answer = 0
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
visited = [[0] * 2001 for _ in range(2001)]
maps = [[0] * 2001 for _ in range(2001)]
# start = list()
start = [(1000, 1000)]
queue = deque([(1000, 1000)])

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    x1 = (x1 + 500) * 2
    y1 = (y1 + 500) * 2
    x2 = (x2 + 500) * 2
    y2 = (y2 + 500) * 2
    
    for i in range(x1, x2 + 1):
        maps[y1][i] = 1
        maps[y2][i] = 1
    
    for i in range(y1, y2 + 1):
        maps[i][x1] = 1
        maps[i][x2] = 1

    start.append((y1, x1))

for y, x in start:
    if not visited[y][x]:
        bfs(y, x)
        answer += 1

print(answer - 1)
