import sys
from collections import deque


def bfs(limit):
    visited = [False] * (n + 1)
    visited[a] = True
    queue = deque([a])
    while queue:
        x = queue.popleft()

        if x == b:
            return True

        for i, c in graph[x]:
            if not visited[i] and limit <= c:
                queue.append(i)
                visited[i] = True

    return False


input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

a, b = map(int, input().split())

result = 0
start, end = 1, 1000000000
while start <= end:
    mid = (start + end) // 2
    if bfs(mid):
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
