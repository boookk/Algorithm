import sys
import heapq
input = sys.stdin.readline


def dijkstra():
    q = []
    heapq.heappush(q, (-sys.maxsize, s))

    visited = [0] * (n + 1)
    visited[s] = sys.maxsize

    while q:
        cur_w, cur_h = heapq.heappop(q)
        cur_w = -cur_w

        if visited[cur_h] > cur_w:
            continue

        for next_w, next_h in graph[cur_h]:
            tmp = min(cur_w, next_w)
            if visited[next_h] < tmp:
                visited[next_h] = tmp
                heapq.heappush(q, (-tmp, next_h))

    return visited[e]


n, m = map(int, input().split())
s, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    h1, h2, k = map(int, input().split())
    graph[h1].append([k, h2])
    graph[h2].append([k, h1])

print(dijkstra())
