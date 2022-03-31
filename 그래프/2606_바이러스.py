def dfs(v):
    if visited[v]:
        return

    visited[v] = True
    for i in graph[v]:
        dfs(i)


n = int(input())
edge = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(edge):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

visited = [False] * (n + 1)
dfs(1)
# 시작 정점을 제외해야 하기 때문에 -1
print(visited.count(True) - 1)
