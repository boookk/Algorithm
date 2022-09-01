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


n, m = map(int, input().split())

parents = [i for i in range(n + 1)]
edges = list()
ans = 0
cnt = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

exit = list(map(int, input().split()))

for i in range(n):
    edges.append((exit[i], 0, i + 1))

edges.sort()

for cost, u, v in edges:
    if union(u, v):
        ans += cost
        cnt += 1
        
        if cnt == n:
            break

print(ans)
