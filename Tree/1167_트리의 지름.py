"""
임의의 노드에서 가장 거리가 있는 노드를 구하고, 그 노드를 시작으로 가장 먼 노드와의 거리를 구하면 된다.
"""
import sys
from collections import deque


def bfs(start):
    visited = [-1] * (v + 1)
    queue = deque([start])
    visited[start] = 0
    max_ = [0, 0]       # 노드 번호, 거리 합

    while queue:
        node = queue.popleft()
        for i, dis in graph[node]:
            if visited[i] == -1:
                queue.append(i)
                visited[i] = visited[node] + dis
                if visited[i] > max_[1]:
                    max_ = i, visited[i]
    return max_


v = int(input())
graph = [[] for _ in range(v+1)]
for _ in range(v):
    tmp = list(map(int, sys.stdin.readline().split()))
    for i in range(1, len(tmp) - 1, 2):
        graph[tmp[0]].append((tmp[i], tmp[i + 1]))

node, dis = bfs(1)
node, dis = bfs(node)
print(dis)
