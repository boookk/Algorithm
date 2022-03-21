import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())        # 과목의 수, 선수 조건의 수
inDegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
dp = [0] * n
for _ in range(m):
    i, j = map(int, input().split())
    graph[i].append(j)
    inDegree[j] += 1

queue = deque()
for i in range(1, n + 1):
    if inDegree[i] == 0:
        queue.append(i)
        dp[i - 1] += 1

while queue:
    x = queue.popleft()
    for i in graph[x]:
        inDegree[i] -= 1

        if inDegree[i] == 0:
            queue.append(i)
            dp[i - 1] = dp[x - 1] + 1
            
print(*dp)
