"""
1. 벽 3개를 세울 수 있는 모든 경우를 구한다.
2. 벽 3개가 만들어지면, bfs를 통해 바이러스가 퍼진 후의 연구소(graph)를 구한다.
  - 이 때, 변수 graph를 깊은 복사를 하여 복사된 graph를 이용하여 구해야 한다.
3. 바이러스가 퍼진 후의 연구소 상태에서 0의 개수를 카운팅하여 변수 result의 값을 갱신한다.
"""
import sys
from collections import deque
import copy

input = sys.stdin.readline


def make_wall(start, count):
    global result
    if count == 3:
        cp_graph = copy.deepcopy(graph)
        for i, j in virus:
            bfs(cp_graph, i, j)
        result = max(result, sum(row.count(0) for row in cp_graph))
    else:
        for i in range(start, n * m):
            r, c = divmod(i, m)
            if graph[r][c] == 0:
                graph[r][c] = 1
                make_wall(i, count + 1)
                graph[r][c] = 0


def bfs(cp_graph, x, y):
    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                continue

            if cp_graph[nx][ny] == 0:
                cp_graph[nx][ny] = 2
                queue.append((nx, ny))


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
virus = [[i, j] for i in range(n) for j in range(m) if graph[i][j] == 2]
result = 0

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

make_wall(0, 0)
print(result)
