"""
PyPy3로 제출했다.
"""
import sys
from collections import deque


def bfs(start):
    cnt = 0
    queue = deque([start])
    visit = [False] * n
    visit[start - 1] = True

    while queue:
        x = queue.popleft()

        for i in graph[x]:
            if not visit[i - 1]:
                queue.append(i)
                visit[i - 1] = True
                cnt += 1

    return cnt


input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

ans = [0] * (n + 1)
for i in range(1, n + 1):
    if not graph[i]:
        continue
    ans[i] = bfs(i)

for i in range(1, n + 1):
    if ans[i] == max(ans):
        print(i, end=' ')
