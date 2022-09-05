import sys
from collections import deque
input = sys.stdin.readline


def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]


def union(a, b):
    a = find(a)
    b = find(b)

    if a == b: return False

    if a < b:
        parents[b] = a
    else:
        parents[a] = b

    return True


def bfs(start):
    queue = deque([(start, 0)])
    visited = [False] * (n + 1)
    visited[start] = True

    while queue:
        cur_node, cur_cost = queue.popleft()

        for next_node, next_cost in graph[cur_node]:
            if not visited[next_node]:
                visited[next_node] = True
                tmp = max(cur_cost, next_cost)
                dp[start][next_node] = tmp
                queue.append((next_node, tmp))


n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]

edges.sort(key=lambda x: x[2])

parents = [i for i in range(n + 1)]
graph = [[] for _ in range(n + 1)]
dp = [[0] * (n + 1) for _ in range(n + 1)]

total_cost = 0
cnt = 0

for u, v, cost in edges:
    if union(u, v):
        total_cost += cost
        cnt += 1
        graph[u].append([v, cost])
        graph[v].append([u, cost])
        if cnt == n - 1:
            break

for i in range(1, n + 1):
    bfs(i)

q = int(input())
for _ in range(q):
    x, y = map(int, input().split())
    print(total_cost - dp[x][y])
