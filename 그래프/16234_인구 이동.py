"""
PyPy3로 제출했다.
그럼에도 불구하고 인구가 이동해야 나라를 미리 카운팅하지 않고 len(move)를 사용하게 되면 시간 초과로 문제가 틀렸다고 채점된다.
그리고 인구이동이 발생하는 날을 카운팅할 때 bfs 함수 안에서 하지 않고 밖에서 해야 한다. 
"""
import sys
from collections import deque


def bfs(x, y, visited):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    global is_move
    people = graph[x][y]
    visited[x][y] = True
    move = [(x, y)]
    cnt = 1

    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or nx >= n or ny <= -1 or ny >= n or visited[nx][ny]:
                continue

            if l <= abs(graph[x][y] - graph[nx][ny]) <= r:
                visited[nx][ny] = True
                move.append((nx, ny))
                people += graph[nx][ny]
                queue.append((nx, ny))
                cnt += 1

    people = people // cnt

    if cnt > 1:
        for x, y in move:
            graph[x][y] = people
        is_move = True


input = sys.stdin.readline

n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
ans = 0

while True:
    is_move = False
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i, j, visited)

    if is_move:
        ans += 1
    else:
        break

print(ans)
