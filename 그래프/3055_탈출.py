"""
덱의 첫 번째에 고슴도치의 위치를 넣고 다음에 물이 있는 위치를 넣으면 시간마다 고슴도치가 이동하는 부분과 물이 차는 부분을 구하지 않아도 된다.
덱에서 고슴도치의 위치가 나온다면 상하좌우로 고슴도치가 이동할 수 있는 부분을 체크한다.
물의 위치가 나온다면 돌이나 동굴이 있는 부분을 제외하고는 상하좌우에 물을 채운다.
"""
import sys
from collections import deque


def bfs():
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    visited = [[False] * c for _ in range(r)]

    while queue:
        x, y = queue.popleft()

        if graph[cave_x][cave_y] == 'S':
            return visited[cave_x][cave_y]

        if not visited[x][y] and graph[x][y] == 'S':
            visited[x][y] = 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or nx >= r or ny <= -1 or ny >= c:
                continue

            if graph[x][y] == '*' and (graph[nx][ny] == '.' or graph[nx][ny] == 'S'):
                graph[nx][ny] = '*'
                queue.append((nx, ny))
            if graph[x][y] == 'S' and (graph[nx][ny] == '.' or graph[nx][ny] == 'D'):
                graph[nx][ny] = 'S'
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

    return 'KAKTUS'


input = sys.stdin.readline

r, c = map(int, input().split())
cave_x, cave_y = 0, 0
queue = deque()
graph = []
for i in range(r):
    graph.append(list(input().rstrip()))
    for j in range(c):
        if graph[i][j] == 'D':
            cave_x, cave_y = i, j
        elif graph[i][j] == 'S':
            queue.appendleft((i, j))
        elif graph[i][j] == '*':
            queue.append((i, j))

print(bfs())
