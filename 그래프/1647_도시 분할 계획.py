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
parents = [i for i in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()

ans = 0
last = 0
for w, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        ans += w
        last = w

print(ans - last)
