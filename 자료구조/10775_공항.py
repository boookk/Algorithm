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


G = int(input())
P = int(input())

answer = 0
parents = {i: i for i in range(G + 1)}

for _ in range(P):
    x = find(int(input()))
    
    if not x:
        break
    
    union(x, x- 1)
    answer += 1

print(answer)
