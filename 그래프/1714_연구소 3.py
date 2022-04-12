"""
m개 이상의 바이러스 중 m개의 바이러스만 활성화시켰을 때 빈 곳에 바이러스를 둘 수 있는 최소 시간을 구해야 한다.
그렇기 때문에 바이러스의 조합을 구하여 bfs를 진행하였다.
시간 제한이 매우 타이트하기 때문에 bfs 진행하는 과정에서 이전의 시간보다 크거나 같으면 중단한다.

처음에 최소 시간을 구할 때 visited에 시간을 저장했지만,
시간을 구할 때 비활성화된 바이러스를 활성화시켰을 때를 제외해야 하고, 
비활성화된 바이러스를 지나 빈곳으로 도착하면 제외했던 시간을 포함시켜야 하는 등 복잡한 경우의 수가 있다.
이를 기존 bfs와 달리 for _ in range(len(queue)) 부분을 추가하고 이 부분을 시작하기 전에 시간을 증가시켜 해결했다.
"""
import sys
from collections import deque
from itertools import combinations


def bfs(v, left):
    global ans

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    visited = [[False] * n for _ in range(n)]
    queue = deque([pos for pos in v])

    time = 0

    while queue:
        if not left:
            break
        time += 1

        if time >= ans:
            return

        for _ in range(len(queue)):
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx <= -1 or nx >= n or ny <= -1 or ny >= n or visited[nx][ny]:
                    continue

                if graph[nx][ny] != 1:
                    queue.append((nx, ny))
                    visited[nx][ny] = True

                if not graph[nx][ny]:
                    left -= 1

    if not left:
        ans = time


input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
virus = deque()
zero = 0
ans = float('inf')

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] == 2:
            virus.append((i, j))
        if graph[i][j] == 0:
            zero += 1

for v in combinations(virus, m):
    bfs(v, zero)

print(-1 if ans == float('inf') else ans)
