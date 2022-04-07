"""
방문을 확인하는 리스트의 크기를 (n과 k 중 큰 수 + 1)로 잡았다가 100001로 바꾸었다.
그 이유는 n에서 k까지 가는 최단 경로가 n * 2를 한 후 거꾸로 가는 경우가 있을 수도 있기 때문이다.
"""
import sys
from collections import deque


def bfs():
    queue = deque([n])
    visited[n] = 0

    while queue:
        x = queue.popleft()

        if x == k:
            break
        if 0 < 2 * x < MAX and visited[2 * x] == -1:
            queue.appendleft(2 * x)
            visited[2 * x] = visited[x]
        if x - 1 >= 0 and visited[x - 1] == -1:
            queue.append(x - 1)
            visited[x - 1] = visited[x] + 1
        if x + 1 < MAX and visited[x + 1] == -1:
            queue.append(x + 1)
            visited[x + 1] = visited[x] + 1


input = sys.stdin.readline
n, k = map(int, input().split())
MAX = 100001
visited = [-1] * MAX
bfs()
print(visited[k])
