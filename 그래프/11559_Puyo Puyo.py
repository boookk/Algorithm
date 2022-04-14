"""
내가 생각하는 이 문제의 포인트는 정렬이다.
해당 블록을 터트리기 위해 위에 블록을 당겨왔는데,
터트릴 블럭을 위쪽부터 없애야 블록을 당기면서 좌표가 변하지 않는다.
예를 들어, 맨 아래 블록 하나를 터트리고 그 위의 블록을 터트리는 경우가 있다.
맨 아래 블록을 터트리면서 그 위의 블록의 좌표값은 +1이 되어 다음에 블록을 터트릴 때 누락된다.
"""

import sys
from collections import deque


def bfs(x, y):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    visited[x][y] = True
    queue = deque([(x, y)])
    tmp = [(x, y)]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or nx >= n or ny <= -1 or ny >= m or visited[nx][ny]:
                continue

            if graph[nx][ny] == graph[x][y]:
                visited[nx][ny] = True
                tmp.append((nx, ny))
                queue.append((nx, ny))

    return tmp if len(tmp) >= 4 else []


input = sys.stdin.readline
n, m = 12, 6
graph = [list(input().rstrip()) for _ in range(n)]
ans = 0

while True:
    visited = [[False] * m for _ in range(n)]

    changed_block = []
    for i in range(n - 1, -1, -1):
        if graph[i] == ['.'] * m:
            break
        for j in range(m):
            if not visited[i][j] and not graph[i][j] == '.':
                block = bfs(i, j)

                if not block:
                    continue

                changed_block.append(block)

    if not changed_block:
        break
        
    changed_block.sort()
    for block in changed_block:
        for x, y in sorted(block):
            while graph[x][y] != '.' and x > 0:
                graph[x][y] = graph[x - 1][y]
                x -= 1
            graph[x][y] = '.'

    ans += 1
print(ans)
