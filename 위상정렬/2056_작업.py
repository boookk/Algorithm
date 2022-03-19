import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
inDegree = [0] * (n + 1)
queue = deque()
dp = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
time = [0]

for i in range(1, n + 1):
    tmp = list(map(int, input().split()))       # 작업 시간, 선행 관계에 있는 작업 수, 작업들 번호
    time.append(tmp[0])

    data = tmp[2:]
    for d in data:
        inDegree[d] += 1
        graph[i].append(d)

for i in range(1, n + 1):
    if inDegree[i] == 0:
        queue.append(i)
        dp[i] = time[i]

while queue:
    x = queue.popleft()

    for i in graph[x]:
        inDegree[i] -= 1
        dp[i] = max(dp[i], dp[x] + time[i])
        if inDegree[i] == 0:
            queue.append(i)

print(max(dp))
