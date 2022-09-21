import sys
from collections import deque
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline


def find_circular_station(depth, start, idx):
    visited[idx] = True
    for i in graph[idx]:
        if not visited[i]:
            find_circular_station(depth + 1, start, i)
        elif start == i and depth > 1:
            isCycle[start] = True
            return


def bfs():
    queue = deque()
    
    for i in range(n):
        if isCycle[i]:
            queue.append(i)
            dist[i] = 0
    
    while queue:
        x = queue.popleft()
        
        for i in graph[x]:
            if dist[i] == -1:
                queue.append(i)
                dist[i] = dist[x] + 1



n = int(input())

graph = [[] for _ in range(n)]
isCycle = [False] * n
dist = [-1] * n

for _ in range(n):
    u, v = map(int, input().split())
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)

for i in range(n):
    visited = [False] * n
    find_circular_station(0, i, i)

bfs()

print(*dist)
