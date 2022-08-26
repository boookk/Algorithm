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


n, m = map(int, input().split())

edges = list()

for _ in range(m + 1):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

edges.sort(key=lambda x: x[2])

parents = [i for i in range(n + 1)]
max_route = 0
for i in range(m + 1):
    u, v, d = edges[i]
    if find(u) != find(v):
        union(u, v)
        max_route += d

parents = [i for i in range(n + 1)]
min_route = 0
for i in range(m, -1, -1):
    u, v, d = edges[i]
    if find(u) != find(v):
        union(u, v)
        min_route += d

print((n - max_route) ** 2 - (n - min_route) ** 2)
