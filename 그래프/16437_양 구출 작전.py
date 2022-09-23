import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline


def dfs(v):
    total = info[v]
    for i in graph[v]:
        total += dfs(i)
    
    if total < 0:
        return 0
    else:
        return total


n = int(input())

graph = [[] for _ in range(n)]
visited = [False] * n
info = [0]

for i in range(1, n):
    t, a, p = input().split()
    a = int(a) if t == 'S' else -int(a)
    graph[int(p) - 1].append(i)
    info.append(a)

print(dfs(0))
