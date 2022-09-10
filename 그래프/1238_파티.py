import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize


def dijkstra(start):
    queue = list()
    heapq.heappush(queue, [0, start])

    visited = [INF] * (n + 1)
    visited[start] = 0

    while queue:
        dist, cur = heapq.heappop(queue)

        if visited[cur] < dist:
            continue

        for next_node, next_dist in graph[cur]:
            tmp = next_dist + dist

            if visited[next_node] > tmp:
                visited[next_node] = tmp
                heapq.heappush(queue, (tmp, next_node))

    return visited


n, m, x = map(int, input().split())

ans = 0
result = [[]]
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, cost = map(int, input().split())
    graph[u].append([v, cost])

for i in range(1, n + 1):
    result.append(dijkstra(i))

for i in range(1, n + 1):
    ans = max(ans, result[i][x] + result[x][i])

print(ans)
