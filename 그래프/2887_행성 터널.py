import sys
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


n = int(input())
locations = [list(map(int, input().split())) + [i] for i in range(n)]

parents = [i for i in range(n)]
edges = list()

ans = 0
cnt = 0

for i in range(3):
    locations.sort(key=lambda x: x[i])
    for j in range(n - 1):
        edges.append((abs(locations[j][i] - locations[j + 1][i]), locations[j][3], locations[j + 1][3]))

edges.sort()

for cost, u, v in edges:
    if union(u, v):
        ans += cost
        cnt += 1
        if cnt == n - 1:
            break

print(ans)
