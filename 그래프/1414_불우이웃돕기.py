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

parents = [i for i in range(n + 1)]
edges = list()

alpha = {chr(96 + i): i for i in range(1, 27)}
alpha.update({chr(38 + i): i for i in range(27, 53)})

result = 0
total = 0
cnt = 0

for i in range(n):
    data = input().rstrip()
    for j in range(n):
        if data[j] != '0':
            tmp = alpha[data[j]]
            edges.append((tmp, i, j))
            total += tmp

edges.sort()


for cost, i, j in edges:
    if find(i) != find(j):
        union(i, j)
        cnt += 1
        result += cost
        if cnt == n - 1:
            break

print(total - result if cnt == n - 1 else -1)
