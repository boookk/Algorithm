import sys
input = sys.stdin.readline
INF = sys.maxsize


def bf():
    dist[1] = 0
    
    for i in range(1, n + 1):
        for u in range(1, n + 1):
            for v, c in graph[u]:
                if dist[v] > dist[u] + c:
                    dist[v] = dist[u] + c
                    if i == n:
                        return True
    
    return False


T = int(input())
for _ in range(T):
    n, m, w = map(int, input().split())
    
    graph = [[] for _ in range(n + 1)]
    dist = [INF] * (n + 1)
    
    for _ in range(m):
        s, e, c = map(int, input().split())
        graph[s].append((e, c))
        graph[e].append((s, c))
    
    for _ in range(w):
        s, e, c = map(int, input().split())
        graph[s].append((e, -c))
    
    print("YES" if bf() else "NO")
