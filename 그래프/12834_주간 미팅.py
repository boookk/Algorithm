import sys
import heapq
sys.stdin = open('data.txt', 'r')
input = sys.stdin.readline
INF = sys.maxsize


def dijkstra(start):
    dist = [INF for _ in range(v + 1)]
    dist[start] = 0
    
    q = []
    heapq.heappush(q, [0, start])
    
    while q:
        cur_d, cur_v = heapq.heappop(q)
        
        if dist[cur_v] < cur_d:
            continue
        
        for next_v, next_d in graph[cur_v]:
            tmp = next_d + cur_d
            if dist[next_v] > tmp:
                dist[next_v] = tmp
                heapq.heappush(q, [tmp, next_v])
    
    return dist


n, v, e = map(int, input().split())
a, b = map(int, input().split())
houses = list(map(int, input().split()))

graph = [[] for _ in range(v + 1)]
for _ in range(e):
    h1, h2, d = map(int, input().split())
    graph[h1].append((h2, d))
    graph[h2].append((h1, d))

dist_a = dijkstra(a)
dist_b = dijkstra(b)

ans = 0
for house in houses:
    a_ = dist_a[house]
    b_ = dist_b[house]
    
    ans = ans - 1 if a_ == INF else ans + a_
    ans = ans - 1 if b_ == INF else ans + b_

print(ans)
