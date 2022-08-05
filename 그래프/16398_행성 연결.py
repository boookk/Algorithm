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
grid = [list(map(int, input().split())) for _ in range(n)]

parents = [i for i in range(n)]
edges = []
for i in range(n):
    for j in range(i + 1, n):
        edges.append((grid[i][j], i, j))

edges.sort()

ans = 0
for cost, x, y in edges:
    if find(x) != find(y):
        union(x, y)
        ans += cost

print(ans)
