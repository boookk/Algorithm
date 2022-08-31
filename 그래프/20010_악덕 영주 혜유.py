import sys
input = sys.stdin.readline


def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]


def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parents[b] = a
    else:
        parents[a] = b


def dfs(idx, total):
    global max_cost, start_node

    if total > max_cost:
        max_cost = total
        start_node = idx

    for next_node, next_cost in graph[idx]:
        if not visited[next_node]:
            visited[next_node] = True
            dfs(next_node, total + next_cost)


n, k = map(int, input().split())

ans = 0
cnt = 0
max_cost = 0
start_node = 0

edges = list()
parents = [i for i in range(n + 1)]
graph = [[] for _ in range(n)]

for i in range(k):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()

for cost, u, v in edges:
    if find(u) != find(v):
        union(u, v)
        ans += cost
        cnt += 1
        graph[u].append([v, cost])
        graph[v].append([u, cost])

        if cnt == n - 1:
            break

visited = [False] * n
visited[start_node] = True
dfs(start_node, 0)

visited = [False] * n
visited[start_node] = True
dfs(start_node, 0)

print(ans)
print(max_cost)
