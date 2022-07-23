"""
리프 노드를 bfs로 찾아도 된다.
"""
import sys

input = sys.stdin.readline

n, w = map(int, input().split())
graph = [0] * (n + 1)
leaf = n - 1
for _ in range(n - 1):
    v, u = map(int, input().split())
    graph[v] += 1
    graph[u] += 1
    
    if v != 1 and graph[v] == 2:
        leaf -= 1
    if u != 1 and graph[u] == 2:
        leaf -= 1

print(w / leaf)
