"""
벨만 포드 알고리즘을 이용하여 가중치가 음수일 경우에도 최단 거리를 구할 수 있도록 하였다.
다익스트라 알고리즘과의 차이점이라면 방문하지 않은 노드 차례로 방문하며 최단 거리를 구하기 때문에
가중치가 음수일 경우에는 최단 거리를 구할 수 없다.
벨만 포드 알고리즘의 경우 매번 모든 간선을 확인하여 최단 거리를 구하기 때문에 음수일 경우에도 최단 거리를 구할 수 있으며,
문제에서 요구한 -∞ 조건도 확인할 수 있다.
"""
import sys


def bf():
    dist[1] = 0
    
    for i in range(n):
        for u in range(1, n + 1):
            for v, w in graph[u]:
                if dist[u] != float('inf') and dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    if i == n - 1:
                        return False
    
    return True


input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

dist = [float('inf')] * (n + 1)
if bf():
    for d in dist[2:]:
        print(d if d != float('inf') else -1)
else:
    print(-1)
