"""
그래프의 높이가 5인지 확인하면 된다.
"""
import sys


def dfs(num, cnt):
    if cnt == 4:
        print(1)
        exit(0)

    for i in graph[num]:
        if visited[i]:
            continue

        visited[i] = True
        dfs(i, cnt + 1)
        visited[i] = False


input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

visited = [False] * n
for i in range(n):
    visited[i] = True
    dfs(i, 0)
    visited[i] = False

print(0)
