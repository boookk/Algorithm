import sys


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)

    if a in truth and b in truth:
        return

    if a in truth:
        parent[b] = a
    elif b in truth:
        parent[a] = b
    else:
        if a > b:
            parent[a] = b
        else:
            parent[b] = a


input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
graph = []

truth = list(map(int, input().split()))[1:]

for _ in range(m):
    tmp = list(map(int, input().split()))
    num, people = tmp[0], tmp[1:]

    for i in range(num - 1):
        union(people[i], people[i + 1])

    graph.append(people)

ans = 0
for g in graph:
    for i in range(len(g)):
        if find(g[i]) in truth:
            break
    else:
        ans += 1
print(ans)
