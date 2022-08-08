import sys
from collections import deque
input = sys.stdin.readline


def bfs(root):
    global cnt
    queue = deque([root])
    
    while queue:
        cur = queue.popleft()
        
        for next in graph[cur]:
            if not visited[next]:
                queue.append(next)
                visited[next] = True
                cnt += 1


n, m = map(int, input().split())
vertex = {chr(i + 65): i  for i in range(n)}
graph = {v: [] for v in vertex.keys()}
visited = {chr(i): False for i in range(65, 65 + n)}
root = [True] * n

for _ in range(m):
    a, b = input().split()
    graph[a].append(b)
    root[vertex[b]] = False

arrest = input().split()

for a in arrest[1:]:
    visited[a] = True

cnt = 0
for k, v in vertex.items():
    if root[v] and not visited[k]:
        bfs(k)
print(cnt)
