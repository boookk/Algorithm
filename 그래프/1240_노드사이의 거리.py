import sys
from collections import deque


def bfs(v, u):
    visited = [False] * (n + 1)
    queue = deque([(v, 0)])
    visited[v] = True
    
    while queue:
        v, d = queue.popleft()
        
        if v == u:
            return d
        
        for i, dist in graph[v]:
            if visited[i]:
                continue
            
            queue.append((i, d + dist))
            visited[i] = True


input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    v, u, d = map(int, input().split())
    graph[v].append((u, d))
    graph[u].append((v, d))

for _ in range(m):
    v, u = map(int, input().split())
    
    print(bfs(v, u))
