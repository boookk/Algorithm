"""
최소 스패닝 트리와 탐색 문제가 섞였다.
2차원이라 어렵게 느껴졌으나, 그동안 학습한 것을 응용하기 좋은 문제였다.
더불어 딕셔너리 get을 활용하여 difualt 값을 사용할 수 있음을 되새길 수 있었다.
"""
import sys
from collections import deque
input = sys.stdin.readline


def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]


def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parents[b] = a
    else:
        parents[a] = b


def bfs(location):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    queue = deque([location])
    visited = [[0] * n for _ in range(n)]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny] or grid[nx][ny] == '1':
                continue

            queue.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1

    for loc in locations:
        if visited[loc[0]][loc[1]] > 0:
            edges.append((visited[loc[0]][loc[1]], nodes[location], nodes[loc]))


n, m = map(int, input().split())

edges = list()
parents = [i for i in range(m + 1)]
grid = [list(input().rstrip()) for _ in range(n)]
nodes = dict()
locations = list()
cnt = 0

for i in range(n):
    for j in range(n):
        if grid[i][j] in ['S', 'K']:
            locations.append((i, j))
            nodes[(i, j)] = cnt
            cnt += 1

for loc in locations:
    bfs(loc)

edges.sort()

ans = 0
for cost, u, v in edges:
    if m == 0:
        break

    if find(u) != find(v):
        union(u, v)
        ans += cost
        m -= 1

print(-1 if m else ans)
