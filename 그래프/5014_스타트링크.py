"""
건물의 층수가 정해져있기 때문에 방문 체크하는 리스트는 건물의 층수만큼의 크기로 만든다.
"""
import sys
from collections import deque


def bfs():
    queue = deque([s])
    visited[s] = 0

    while queue:
        x = queue.popleft()

        if x == g:
            return visited[g]
        if x + u <= f and visited[x + u] == -1:
            queue.append(x + u)
            visited[x + u] = visited[x] + 1
        if x - d > 0 and visited[x - d] == -1:
            queue.append(x - d)
            visited[x - d] = visited[x] + 1

    return "use the stairs"

input = sys.stdin.readline
f, s, g, u, d = map(int, input().split())
visited = [-1] * (f + 1)
print(bfs())
