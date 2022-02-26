"""
1167 트리의 지름과 비슷한 문제로 트리의 거리 대신 가중치를 이용하여 가장 긴 지름을 출력한다.
"""
import sys
from collections import deque


def bfs(start):
    visit = [-1] * (n + 1)
    queue = deque([start])
    visit[start] = 0
    max_ = [0, 0]       # 노드 번호, 가중치 합

    while queue:
        node = queue.popleft()
        for i, w in graph[node]:
            if visit[i] == -1:
                queue.append(i)
                visit[i] = visit[node] + w
                if visit[i] > max_[1]:
                    max_ = i, visit[i]
    return max_


n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    parents, child, w = map(int, sys.stdin.readline().split())
    graph[parents].append([child, w])
    graph[child].append([parents, w])

node, w = bfs(1)
node, w = bfs(node)
print(w)
