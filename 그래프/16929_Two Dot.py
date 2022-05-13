"""
사이클을 이루었는지 점의 개수를 카운팅하지 않아도 된다.
현재 지점을 기준으로 다음에 방문할 지점이 바로 이전에 방문한 지점이 아니라면 탐색을 진행한다.
이 때 다음에 탐색할 지점이 이미 방문한 지점이라면 사이클이 이루어진다고 생각하면 된다.
"""
import sys

input = sys.stdin.readline


def dfs(xi, yi, x, y):
    if visited[x][y]:
        return True
    
    visited[x][y] = True
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
            continue
        
        if xi != nx or yi != ny:
            if graph[nx][ny] == graph[x][y]:
                if dfs(x, y, nx, ny):
                    return True
            
    return False


n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for i in range(n):
    for j in range(m):
        visited = [[False] * m for _ in range(n)]
        if dfs(0, 0, i, j):
            print('Yes')
            exit()
else:
    print('No')
