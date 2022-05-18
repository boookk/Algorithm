"""
visited를 3차원으로 만들어 그람을 소지하고 있는 유무에 따라 최소 시간을 따로 구했었다.
이러한 방법보다 공주님과 그람의 위치를 이용하여 맨하탄 거리를 구한다면 복잡도를 줄일 수 있다.
"""
import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    
    visited = [[0 for _ in range(m)] for _  in range(n)]

    queue = deque([(0, 0)])
    visited[0][0] = 1
    distGram = 10001

    while queue:
        x, y = queue.popleft()
        
        if x == n - 1 and y == m - 1:
            return min(visited[x][y] - 1, distGram)
        
        if graph[x][y] == 2:
            distGram = visited[x][y] + (n - 1 - x) + (m - 1 - y) - 1
            
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
                
            if nx <= -1 or nx >= n or ny <= -1 or ny >= m or visited[nx][ny]:
                continue
            
            if graph[nx][ny] == 0 or graph[nx][ny] == 2:
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
        
    return distGram
    

n, m, t = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

ans = bfs()
print('Fail' if ans > t else ans)
