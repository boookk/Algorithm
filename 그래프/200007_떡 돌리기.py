import sys
import heapq
input = sys.stdin.readline


def dijkstra():
    dist = [sys.maxsize for _ in range(n)]
    dist[y] = 0
    q = []
    heapq.heappush(q, [0, y])

    while q:
        cur_dist, cur = heapq.heappop(q)

        for v, d in graph[cur]:
            tmp = cur_dist + d
            if dist[v] > tmp:
                dist[v] = tmp
                heapq.heappush(q, [tmp, v])

    return dist


n, m, x, y = map(int, input().split())

graph = [[] for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

result = dijkstra()

for dist in result:
    if dist > x // 2:
        print(-1)
        break
else:
    result.sort()

    day = 1
    cur = 0

    for dist in result:
        if cur + 2 * dist <= x:
            cur += 2 * dist
        else:
            day += 1
            cur = 2 * dist
    print(day)
