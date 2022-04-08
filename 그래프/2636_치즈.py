"""
그래프 탐색 문제를 풀 때 대부분 1인 부분만을 찾아 탐색을 진행한다.
그러나 이 문제는 0인 부분을 찾아 탐색한다는 점에서 새로웠다.
"""
import sys
from collections import deque


def bfs():
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    queue = deque([(0, 0)])

    cnt = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or nx >= n or ny <= -1 or ny >= m or visited[nx][ny]:
                continue

            if graph[nx][ny]:
                graph[nx][ny] = 0
                cnt += 1
            else:
                queue.append((nx, ny))

            visited[nx][ny] = 1
    return cnt


input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

ans = 0
cheese = 0

while True:
    count = bfs()

    if count < 1:
        break
    ans += 1
    cheese = count

print(ans)
print(cheese)
