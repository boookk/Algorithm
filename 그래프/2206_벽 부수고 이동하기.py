"""
BFS로 풀어야 하는 것은 알았지만, 벽을 부수고 최단 거리를 만족하면 벽을 한 번만 부수고 갈 수 있다는 조건을 구현하기 어려웠다.
인터넷을 찾아보면서 방문 여부를 확인하는 visited 리스트를 3차원으로 생성해야 된다는 것을 알 수 있었다.
"""


from collections import deque
import sys


n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, list(input()))) for _ in range(n)]


def bfs():
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    # [0] * 2 는 벽을 부수지 않고 가는 경우와 벽을 부수고 가는 경우를 따로 저장하기 위한 부분이다.
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

    queue = deque([(0, 0, 0)])
    visited[0][0][0] = 1

    while queue:
        x, y, wall = queue.popleft()

        # 도착 지점이라면,
        if x == n - 1 and y == m - 1:
            return visited[x][y][wall]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위를 벗어났거나, 이미 방문했다면 
            if nx <= -1 or nx >= n or ny <= -1 or ny >= m or visited[nx][ny][wall] != 0:
                continue

            # 벽이 아니라면,
            if graph[nx][ny] == 0:
                queue.append((nx, ny, wall))
                visited[nx][ny][wall] = visited[x][y][wall] + 1

            # 벽을 부수지 않았고 벽이라면, 부수고 이동
            if graph[nx][ny] == 1 and wall == 0:
                queue.append((nx, ny, wall + 1))
                visited[nx][ny][wall + 1] = visited[x][y][wall] + 1

    return -1


print(bfs())
