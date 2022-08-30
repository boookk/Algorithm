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


n = int(input())

edges = list()
parents = [i for i in range(n + 1)]
ans = 0

for i in range(n):
    edges.append((int(input()), 0, i + 1))

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if i == j: continue
        edges.append((data[j], i + 1, j + 1))

edges.sort()

for cost, u, v in edges:
    if find(u) != find(v):
        union(u, v)
        ans += cost

print(ans)
