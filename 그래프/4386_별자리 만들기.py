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
loc = [list(map(float, input().split())) for _ in range(n)]

cost_lst = []
parents = [i for i in range(n)]

for i in range(n - 1):
    for j in range(i + 1, n):
        cost_lst.append((((loc[i][0] - loc[j][0]) ** 2 + (loc[i][1] - loc[j][1]) ** 2) ** 0.5, i, j))

cost_lst.sort()

ans = 0
for cost, x, y in cost_lst:
    if find(x) != find(y):
        union(x, y)
        ans += cost
    
print(round(ans, 2))
