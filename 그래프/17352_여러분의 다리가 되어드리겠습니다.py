import sys


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


input = sys.stdin.readline

n = int(input())
parent = [i for i in range(n + 1)]

for i in range(n - 2):
    v, w = map(int, input().split())
    union(v, w)

answer = []
for i in range(1, n + 1):
    if i == parent[i] and len(answer) < 3:
        answer.append(i)
    
    if len(answer) > 2:
        break
print(*answer)
