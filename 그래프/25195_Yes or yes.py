import sys
from collections import deque
input = sys.stdin.readline


def bfs():   
    if visited[1]:
        return 'Yes'
    
    queue = deque([1])
    visited[1] = True
    
    while queue:
        cur = queue.popleft()
        
        if not graph[cur]:
            return 'yes'
        
        for next in graph[cur]:
            if not visited[next]:
                queue.append(next)
                visited[next] = True
    
    return 'Yes'

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

s = int(input())
fan = list(map(int, input().split()))

visited = [False] * (n + 1)
for f in fan:
    visited[f] = True

print(bfs())
