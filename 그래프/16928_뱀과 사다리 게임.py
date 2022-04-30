import sys
from collections import deque


def bfs():
    queue = deque([1])

    while queue:
        x = queue.popleft()

        if x == 100:
            return

        for i in range(1, 7):
            nx = x + i

            if nx >= 101 or visited[nx]:
                continue

            if nx in ladder.keys():
                nx = ladder[nx]

            if nx in snake.keys():
                nx = snake[nx]

            if not visited[nx]:
                queue.append(nx)
                visited[nx] = visited[x] + 1
                

input = sys.stdin.readline

n, m = map(int, input().split())
visited = [0] * 101

ladder = dict()
snake = dict()

for _ in range(n):
    i, j = map(int, input().split())
    ladder[i] = j

for _ in range(m):
    i, j = map(int, input().split())
    snake[i] = j

bfs()
print(visited[100])
