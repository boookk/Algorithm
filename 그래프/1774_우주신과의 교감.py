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
locations = list()
parents = [i for i in range(n)]

for _ in range(n):
    locations.append(list(map(int, input().split())))

for _ in range(m):
    a, b = map(int, input().split())
    union(a - 1, b - 1)

for i in range(n - 1):
    for j in range(i + 1, n):
        dist = ((locations[i][0] - locations[j][0]) ** 2 + (locations[i][1] - locations[j][1]) ** 2) ** 0.5
        edges.append((dist, i, j))

edges.sort()

ans = 0
for dist, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        ans += dist

print('%.2f' % ans)
