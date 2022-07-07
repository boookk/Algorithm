import sys

def dfs(depth, visited, p):
    global ans
    
    if depth == n:
        ans += p
        return
    
    for i in range(4):
        x, y = visited[-1]
        nx = x + dx[i]
        ny = y + dy[i]
        
        if (nx, ny) in visited:
            continue
        
        visited.append((nx, ny))
        dfs(depth + 1, visited, p * D[i] * 0.01)
        visited.pop()


input = sys.stdin.readline

n, east, west, south, north = map(int, input().split())
D = [east, west, south, north]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

ans = 0
dfs(0, [(0, 0)], 1)
print(ans)
