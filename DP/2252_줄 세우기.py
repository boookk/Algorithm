import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
inDegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
dp = []

for _ in range(m):
    a, b = map(int, input().split())
    inDegree[b] += 1
    graph[a].append(b)

queue = deque()
for i in range(1, n + 1):
    if inDegree[i] == 0:
        queue.append(i)

while queue:
    x = queue.popleft()
    dp.append(x)
    for i in graph[x]:
        inDegree[i] -= 1
        if inDegree[i] == 0:
            queue.append(i)
            
print(*dp)
