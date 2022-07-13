import sys


def dfs(x, y, depth, total):
    global answer
    
    if depth == 3 or answer >= total + max_val * (3 - depth):
        answer = max(answer, total)
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny]:
            continue
        
        if depth == 1:  # ㅏ 모양의 테트로미노를 놓는 
            visited[nx][ny] = True
            dfs(x, y, depth + 1, total + graph[nx][ny])
            visited[nx][ny] = False
        
        visited[nx][ny] = True
        dfs(nx, ny, depth + 1, total + graph[nx][ny])
        visited[nx][ny] = False


input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

answer = 0
max_val = max(map(max, graph))
for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, 0, graph[i][j])
        visited[i][j] = False

print(answer)
