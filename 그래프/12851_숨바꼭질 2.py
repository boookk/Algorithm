import sys
from collections import deque


def bfs():
    global cnt
    m = 0
    visited[n] = 0
    queue = deque([n])

    while queue:
        x = queue.popleft()

        if x == k:
            cnt += 1

        for op in [2 * x, x - 1, x + 1]:
            if 0 <= op < MAX:
                if visited[op] == -1 or visited[op] == visited[x] + 1:
                    visited[op] = visited[x] + 1
                    queue.append(op)


input = sys.stdin.readline
n, k = map(int, input().split())
MAX = 100001
visited = [-1] * MAX
cnt = 0
bfs()
print(visited[k])
print(cnt)
