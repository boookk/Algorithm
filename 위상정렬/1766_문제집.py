import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())
inDegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    i, j = map(int, input().split())
    inDegree[j] += 1
    graph[i].append(j)

heap = []
for i in range(1, n + 1):
    if inDegree[i] == 0:
        heapq.heappush(heap, i)

while heap:
    x = heapq.heappop(heap)
    print(x, end=' ')

    for i in graph[x]:
        inDegree[i] -= 1
        if inDegree[i] == 0:
            heapq.heappush(heap, i)
