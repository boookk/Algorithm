import sys
import heapq

def dijkstra(start):
    cnt = 0
    result = 0
    
    q = []
    heapq.heappush(q, (0, start))
    
    visited = [float('inf')] * (n + 1)
    visited[start] = 0
    
    while q:
        sec, cur = heapq.heappop(q)
        
        for v, t in graph[cur]:
            tmp = sec + t
            if tmp < visited[v]:
                heapq.heappush(q, (tmp, v))
                visited[v] = tmp
    
    for val in visited:
        if val != float('inf'):
            cnt += 1
            if val > result:
                result = val
    
    return cnt, result


input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((a, s))
    
    print(*dijkstra(c))
