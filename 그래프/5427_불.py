"""
PyPy3로 제출하였다.
여기서 방문 체크를 하는 visited리스트를 만들지 않았다.
원본 리스트를 변경하며 if 문에서 현재 위치가 불인지, 상근인지에 따라 다른 조건을 주어 이동시키기 때문이다.
"""
import sys
from collections import deque


def bfs():
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    t = 0
    while queue:
        t += 1
        for _ in range(len(queue)):
            x, y = queue.popleft()

            if graph[x][y] == '@' and (x == 0 or x == h - 1 or y == 0 or y == w - 1):
                return t

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx <= -1 or nx >= h or ny <= -1 or ny >= w:
                    continue

                if graph[x][y] == '@' and graph[nx][ny] == '.':
                    graph[nx][ny] = '@'
                    queue.append((nx, ny))

                if graph[x][y] == '*' and (graph[nx][ny] == '.' or graph[nx][ny] == '@'):
                    graph[nx][ny] = '*'
                    queue.append((nx, ny))

    return 'IMPOSSIBLE'


input = sys.stdin.readline
T = int(input())

for _ in range(T):
    w, h = map(int, input().split())
    graph = []
    queue = deque()

    for i in range(h):
        graph.append(list(input().rstrip()))
        for j in range(w):
            if graph[i][j] == '@':
                queue.appendleft((i, j))
            if graph[i][j] == '*':
                queue.append((i, j))

    print(bfs())
