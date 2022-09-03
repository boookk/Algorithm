import sys
import heapq
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


n, m = map(int, input().split())

parents = [i for i in range(n)]
edges = list()
remain_edges = list()
ans = [0] * n

cnt = 0

for i in range(n):
    data = list(input().rstrip())
    for j in range(i + 1, n):
        if data[j] == 'Y':
            heapq.heappush(edges, [i, j])

if len(edges) < m:
    print(-1)
else:
    while edges:
        u, v = heapq.heappop(edges)
        if union(u, v):
            ans[u] += 1
            ans[v] += 1
            cnt += 1
        else:
            heapq.heappush(remain_edges, [u, v])

    if cnt != n - 1:
        print(-1)
    else:
        for _ in range(m - cnt):
            u, v = heapq.heappop(remain_edges)
            ans[u] += 1
            ans[v] += 1
        print(*ans)
