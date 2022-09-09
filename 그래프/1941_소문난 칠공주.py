import sys
input = sys.stdin.readline


def check(num):
    global cnt
    x, y = divmod(num, 5)
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny]:
            continue
        
        tmp = nx * 5 + ny
        if tmp in princess:
            visited[nx][ny] = 1
            cnt += 1
            check(tmp)


def dfs(depth, y_cnt, idx):
    global cnt, visited, ans
    
    if y_cnt > 3 or 25 - idx < 7 - depth:
        return
    
    if depth == 7:
        cnt = 0
        check(princess[0])
        if cnt == 7:
            ans += 1
        visited = [[0] * n for _ in range(n)]
        return
    
    x, y = divmod(idx, 5)
    princess.append(idx)
    
    if grid[x][y] == 'Y':
        dfs(depth + 1, y_cnt + 1, idx + 1)
    else:
        dfs(depth + 1, y_cnt, idx + 1)

    princess.pop()
    dfs(depth, y_cnt, idx + 1)


n = 5

grid = [list(input().rstrip()) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

visited = [[0] * n for _ in range(n)]
princess = list()
ans = 0

dfs(0, 0, 0)
print(ans)
