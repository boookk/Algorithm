import sys
input = sys.stdin.readline


def dfs(x, y):
    if y == c - 1:
        return True
    
    for dx in [-1, 0, 1]:
        nx = x + dx
        ny = y + 1
        
        if nx < 0 or nx >= r or grid[nx][ny] == 'x' or visited[nx][ny]:
            continue
        
        visited[nx][ny] = True
    
        if dfs(nx, ny):
            return True
    
    return False


r, c = map(int, input().split())
grid = [list(input().rstrip()) for _ in range(r)]

ans = 0
visited = [[False] * c for _ in range(r)]

for i in range(r):
    if dfs(i, 0):
        ans += 1

print(ans)
