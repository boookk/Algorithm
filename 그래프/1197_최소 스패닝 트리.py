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


v, e = map(int, input().split())

edges = list()
parents = [i for i in range(v + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()

ans = 0
for w, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        ans += w

print(ans)
