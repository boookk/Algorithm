import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
s, e = map(int, input().split())
m = int(input())
for _ in range(m):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)


def bfs(x, y):
    queue = deque([x])
    visit = [0] * (n + 1)
    while queue:
        x = queue.popleft()

        for i in graph[x]:
            if not visit[i]:
                queue.append(i)
                visit[i] = visit[x] + 1

    return visit[y]


ans = bfs(s, e)
print(ans if ans else -1)
