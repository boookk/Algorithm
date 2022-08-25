import sys
sys.stdin = open('data.txt', 'r')
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
gender = input().rstrip().split()

parents = [i for i in range(n + 1)]
edges = list()

for _ in range(m):
    edges.append(list(map(int, input().split())))

edges.sort(key=lambda x: x[2])

ans = 0
cnt = 0

for u, v, d in edges:
    if find(u) != find(v) and gender[u - 1] != gender[v - 1]:
        union(u, v)
        ans += d
        cnt += 1
    
    if cnt == n - 1:
        break

print(ans if cnt == n - 1 else -1)
