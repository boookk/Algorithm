import sys
import heapq

def dijkstra():
    visited[1] = 0
    
    q = list()
    heapq.heappush(q, (0, 1))
    
    while q:
        weight, node = heapq.heappop(q)
        
        if visited[node] < weight:
            continue
        
        for v, w in graph[node]:
            tmp = w + weight
            if tmp < visited[v]:
                heapq.heappush(q, (tmp, v))
                visited[v] = tmp


input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    v, u, w = map(int, input().split())
    graph[v].append((u, w))
    graph[u].append((v, w))

visited = [float('inf')] * (n + 1)
dijkstra()
print(visited[n])
