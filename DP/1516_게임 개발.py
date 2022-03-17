import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
time = [0]
inDegree = [0] * (n + 1)
for i in range(1, n + 1):
    tmp = list(map(int, input().split()))
    time.append(tmp[0])
    for j in tmp[1:-1]:
        inDegree[i] += 1
        graph[j].append(i)

queue = deque()
dp = [0] * (n + 1)
for i in range(1, n + 1):
    if inDegree[i] == 0:
        queue.append(i)
        dp[i] = time[i]

while queue:
    v = queue.popleft()
    for u in graph[v]:
        inDegree[u] -= 1
        dp[u] = max(dp[u], dp[v] + time[u])
        if inDegree[u] == 0:
            queue.append(u)

print(*dp[1:], sep='\n')
