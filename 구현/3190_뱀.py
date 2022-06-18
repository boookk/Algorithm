import sys
from collections import deque


input = sys.stdin.readline

n = int(input())
k = int(input())

graph = [[0] * n for _ in range(n)]

for _ in range(k):  # 사과 위치
    x, y = map(int, input().split())
    graph[x - 1][y - 1] = 1

direction = {}
l = int(input())
for _ in range(l):  # 방향 바꾸는 타이밍
    x, c = input().split()
    direction[int(x)] = c

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

ans = 0     # 시간
d = 1       # 뱀의 방향
x, y = 0, 0     # 현재 좌표

snake = deque([[x, y]])

while True:
    ans += 1
    x += dx[d]
    y += dy[d]

    if ans in direction.keys():
        if direction[ans] == 'L':
            d = (d - 1) % 4
        else:
            d = (d + 1) % 4

    if 0 <= x < n and 0 <= y < n:
        if [x, y] in snake:
            break

        if graph[x][y]:
            graph[x][y] = 0
            snake.append([x, y])
        else:
            snake.append([x, y])
            snake.popleft()
    else:
        break

print(ans)
