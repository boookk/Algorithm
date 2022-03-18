import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
inDegree = [0] * (n + 1)
queue = deque()
result = []
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    tmp = list(map(int, input().split()))
    data = tmp[1:]
    for i in range(1, tmp[0]):
        inDegree[data[i]] += 1
        graph[data[i - 1]].append(data[i])

for i in range(1, n + 1):
    if inDegree[i] == 0:
        queue.append(i)

while queue:
    x = queue.popleft()
    result.append(x)

    for i in graph[x]:
        inDegree[i] -= 1
        if inDegree[i] == 0:
            queue.append(i)

if len(result) == n:
    print(*result, sep='\n')
else:
    print(0)
