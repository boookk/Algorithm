"""
처음에 리스트 visited를 2차원으로 만들고 해당 좌표까지 도착하는 최소 시간을 저장하였지만, 메모리 초과가 발생하였다.
그 이유는 방문 체크를 하지 않아 덱에 많은 요소를 넣어버리기 때문이다.
그래서 리스트 visited를 3차원으로 만들고 말처럼 움직였을 때를 포함하여 방문처리해준다.
"""
import sys
from collections import deque


def bfs():
    dx = [-1, 0, 1, 0, -2, -2, -1, -1, 1, 1, 2, 2]
    dy = [0, -1, 0, 1, -1, 1, -2, 2, -2, 2, -1, 1]
    queue = deque([(0, 0, 0, k)])
    visited[0][0][k] = True

    while queue:
        x, y, t, c = queue.popleft()

        if x == h - 1 and y == w - 1:
            return t

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or nx >= h or ny <= -1 or ny >= w:
                continue

            if not graph[nx][ny] and not visited[nx][ny][c]:
                queue.append((nx, ny, t + 1, c))
                visited[nx][ny][c] = True

        if 0 < c:
            for i in range(4, 12):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx <= -1 or nx >= h or ny <= -1 or ny >= w:
                    continue

                if not graph[nx][ny] and not visited[nx][ny][c - 1]:
                    queue.append((nx, ny, t + 1, c - 1))
                    visited[nx][ny][c - 1] = True

    return -1


input = sys.stdin.readline
k = int(input())
w, h = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(h)]
visited = [[[False] * (k + 1) for _ in range(w)] for _ in range(h)]
print(bfs())
