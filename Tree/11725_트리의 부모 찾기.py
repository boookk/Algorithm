"""
처음에 DFS로 문제를 풀었는데, RecursionError가 발생하였다.
그래서 최대 재귀호출 수를 증가하기 보다, BFS로 변경하여 문제를 해결했다.
"""
import sys
from collections import deque


def bfs():
    queue = deque([1])
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not parents[i]:
                parents[i] = v
                queue.append(i)


n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    i, j = map(int, sys.stdin.readline().split())
    graph[i].append(j)
    graph[j].append(i)

parents = [0] * (n+1)
bfs()
print(*parents[2:], sep='\n')
