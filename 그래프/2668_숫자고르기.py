"""
루프가 있는지 확인하기 위해 dfs로 풀었다.
"""
import sys


def dfs(v, s):
  visited[v] = True
  
  for i in graph[v]:
    if not visited[i]:
      dfs(i, s)
    elif visited[i] and s == i:
      result.append(i)


input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
result = []

for i in range(1, n + 1):
  v = int(input())
  graph[i].append(v)

for i in range(1, n + 1):
  visited = [False] * (n + 1)
  dfs(i, i)

print(len(result))
print(*sorted(result), sep='\n')
