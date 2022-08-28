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


n, m, k = map(int, input().split())
power_plant = list(map(int, input().split()))

edges = list()
parents = [i for i in range(n + 1)]
ans = 0

for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))

for i in range(k - 1):
    union(power_plant[i], power_plant[i + 1])

edges.sort()

for w, u, v in edges:
    if find(u) != find(v):
        union(u, v)
        ans += w

print(ans)
