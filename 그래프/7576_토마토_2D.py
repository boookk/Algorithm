"""
이 문제는 7579 문제와 비슷한 문제로, 조금 더 쉬운 문제다.
7579 문제는 3차원에서 BFS를 수행했어야 했으므로 고민을 많이 했던 문제였다.
이 문제는 2차원에서 BFS로 해결하면 되므로 금방 풀 수 있었다.
"""

from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

m, n = map(int, input().split())

graph = []
queue = deque()
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(m):
        if tmp[j] == 1:
            queue.append((i, j))
    graph.append(tmp)

while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
            continue
        if graph[nx][ny] == 0:
            queue.append((nx, ny))
            graph[nx][ny] = graph[x][y] + 1

result = 0
for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
        result = max(result, j)
print(result - 1)
