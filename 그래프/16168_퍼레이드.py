"""
한 붓 그리기 문제의 경우, 홀수인 경로가 2개(출발지, 도착지)이거나, 없어야 한다.
"""
import sys
input = sys.stdin.readline


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)

    if level[a] >= level[b]:
        parent[b] = a
        if level[a] == level[b]:
            level[a] += 1
    else:
        parent[a] = b


v, e = map(int, input().split())
parent = [i for i in range(v + 1)]
graph = [[] for _ in range(v + 1)]
level = [0] * (v + 1)
for _ in range(e):
    a, b = map(int, input().split())
    if find(a) != find(b):
        union(a, b)
    graph[a].append(b)
    graph[b].append(a)

pivot = find(1)
for i in range(2, v + 1):
    if pivot != find(i):
        print('NO')
        exit(0)

cnt = 0
for start_node in range(1, v + 1):
    if len(graph[start_node]) & 1:
        cnt += 1

print('YES' if not cnt or cnt == 2 else 'NO')
