import sys
sys.setrecursionlimit(10 ** 9)


def dfs(v):
    visit[v] = True
    for i in graph[v]:
        if not visit[i]:
            dfs(i)


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    graph[i].append(j)
    graph[j].append(i)

count = 0
visit = [False] * (n + 1)
for i in range(1, n + 1):
    if not visit[i]:
        dfs(i)
        count += 1
print(count)
