from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    cnt = 0

    while queue:
        x, y = queue.popleft()
        cnt += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or nx >= n or ny <= -1 or ny >= n:
                continue
            if not graph[nx][ny]:
                continue
            graph[nx][ny] = 0
            queue.append((nx, ny))
    return cnt


n = int(input())
graph = [list(map(int, list(input()))) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
visited = [[False] * n for _ in range(n)]
result = 0
count = []
for i in range(n):
    for j in range(n):
        if graph[i][j]:
            graph[i][j] = 0
            count.append(bfs(i, j))
            result += 1

print(result)
print(*sorted(count), sep='\n')
