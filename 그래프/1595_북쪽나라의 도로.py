import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline


def dfs(u, dist):
    global node, max_dist
    
    if dist > max_dist:
        node = u
        max_dist = dist
    
    visited[u] = True
    
    for v, d in graph[u]:
        if not visited[v]:
            dfs(v, dist + d)


n = 0
max_dist = 0
node = 1
graph = {i: [] for i in range(10001)}

while True:
    try:
        n += 1
        u, v, d = map(int, input().split())
        graph[u].append((v, d))
        graph[v].append((u, d))
    except:
        break

for _ in range(2):
    visited = [False] * (n + 1)
    dfs(node, 0)

print(max_dist)
