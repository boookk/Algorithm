import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def dfs(x):
    compliment[x] += compliment[superior[x]]
    for v in graph[x]:
        dfs(v)


n, m = map(int, input().split())
superior_list = list(map(int, input().split()))

graph = [[] for _ in range(n + 1)]
compliment = [0] * (n + 1)
superior = [0] * (n + 1)

for i in range(1, n):
    graph[superior_list[i]].append(i + 1)
    superior[i + 1] = superior_list[i]

for _ in range(m):
    i, w = map(int, input().split())
    compliment[i] += w

dfs(1)
print(*compliment[1:])
