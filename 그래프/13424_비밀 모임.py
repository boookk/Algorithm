import sys
import heapq


def dijkstra(loc):
    q = []
    heapq.heappush(q, (0, loc))
    distance[loc] = 0
    
    while q:
        dist, cur = heapq.heappop(q)
        
        if dist > distance[cur]:
            continue
        
        for v, d in graph[cur]:
            tmp = dist + d
            if tmp < distance[v]:
                distance[v] = tmp
                heapq.heappush(q, (tmp, v))


input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    
    k = int(input())
    location = list(map(int, input().split()))
    
    total_dist = [0] * (n + 1)
    for loc in location:
        distance = [float('inf')] * (n + 1)
        dijkstra(loc)

        for i in range(1, n + 1):
            total_dist[i] += distance[i]
    
    min_loc = 0
    min_dist = float('inf')
    for i in range(1, n + 1):
        if min_dist > total_dist[i]:
            min_dist = total_dist[i]
            min_loc = i
    print(min_loc)
