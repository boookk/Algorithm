import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
names = input().split()
m = int(input())
inDegree = {name: 0 for name in names}
graph = {name: [] for name in names}
result = {name: [] for name in names}
ancestor = []

for _ in range(m):
    x, y = input().split()      # y는 x의 조상
    graph[y].append(x)
    inDegree[x] += 1

queue = deque()
for k, v in inDegree.items():
    if v == 0:
        queue.append(k)
        ancestor.append(k)

while queue:
    x = queue.popleft()

    for name in graph[x]:
        inDegree[name] -= 1
        if inDegree[name] == 0:
            result[x] += [name]
            queue.append(name)

print(len(ancestor))
print(*sorted(ancestor))
for k, v in sorted(result.items()):
    print(k, len(v), *sorted(v))
