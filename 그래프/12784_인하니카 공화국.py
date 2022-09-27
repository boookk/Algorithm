import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline


def dfs(u):
    visited[u] = True
    total = 0
    
    for v, d in graph[u]:
        if not visited[v]:
            total += min(d, dfs(v))
    
    return total if total else sys.maxsize

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    
    if n == 1:
        print(0)
    else:
        visited = [False] * (n + 1)
        graph = {i: [] for i in range(1, n + 1)}
        
        for _ in range(m):
            u, v, d = map(int, input().split())
            graph[u].append((v, d))
            graph[v].append((u, d))
        
        print(dfs(1))
