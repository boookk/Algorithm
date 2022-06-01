import sys
sys.setrecursionlimit(10 ** 9)

def dfs(x):
    visited[x] = True
    subtree[x] = 1
    
    for i in graph[x]:
        if not visited[i]:
            dfs(i)
            subtree[x] += subtree[i]


input = sys.stdin.readline

n, r, q = map(int, input().split()) # 정점의 수, 루트 번호, 쿼리 수
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
subtree = [0] * (n + 1)

for i in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dfs(r)

for i in range(q):
    root = int(input())
    print(subtree[root])
